from flask import Blueprint, request, jsonify
from app.models import User, File
from app import db, bcrypt
from app.utils.mailer import send_verification_email
from app.utils.encryption import verify_encrypted_url
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

client_bp = Blueprint('client', __name__)

@client_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(email=data['email'], password_hash=hashed_password, role='Client')
    db.session.add(user)
    db.session.commit()
    send_verification_email(data['email'])
    return jsonify(msg="Signup successful. Verification email sent."), 201

@client_bp.route('/verify/<email>', methods=['GET'])
def verify_email(email):
    user = User.query.filter_by(email=email).first()
    if user:
        user.verified = True
        db.session.commit()
        return jsonify(msg="Email verified."), 200
    return jsonify(msg="Invalid verification link."), 400

@client_bp.route('/login', methods=['POST'])
def client_login():
    data = request.json
    user = User.query.filter_by(email=data['email'], role='Client').first()
    if user and bcrypt.check_password_hash(user.password_hash, data['password']):
        if not user.verified:
            return jsonify(msg="Email not verified."), 403
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token), 200
    return jsonify(msg="Invalid credentials"), 401

@client_bp.route('/files', methods=['GET'])
@jwt_required()
def list_files():
    files = File.query.all()
    return jsonify(files=[{"name": f.file_name, "link": f"/client/download/{f.download_token}"} for f in files]), 200

@client_bp.route('/download/<token>', methods=['GET'])
@jwt_required()
def download_file(token):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user.role != 'Client':
        return jsonify(msg="Access denied"), 403

    file = File.query.filter_by(download_token=token).first()
    if not file:
        return jsonify(msg="Invalid token"), 404

    if not verify_encrypted_url(token, file.file_name):
        return jsonify(msg="Invalid or tampered URL"), 400

    return jsonify(msg="Success", download_link=f"/{file.file_path}"), 200
