from flask import Blueprint, request, jsonify
from app.models import User, File
from app import db, bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import os
from werkzeug.utils import secure_filename
from app.utils.encryption import generate_encrypted_url

ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}
ops_bp = Blueprint('ops', __name__)

@ops_bp.route('/login', methods=['POST'])
def ops_login():
    data = request.json
    user = User.query.filter_by(email=data['email'], role='Ops').first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        token = create_access_token(identity=str(user.id))

        return jsonify(access_token=token), 200
    return jsonify(msg="Invalid credentials"), 401


@ops_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    user_id = get_jwt_identity()          # Get the JWT identity
    user = User.query.get(int(user_id))   # Convert to int if needed

    if not user or user.role != 'Ops':
        return jsonify(msg="Unauthorized"), 403

    file = request.files.get('file')
    if not file:
        return jsonify(msg="No file uploaded"), 400

    filename = secure_filename(file.filename)
    ext = filename.rsplit('.', 1)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        return jsonify(msg="Invalid file type"), 400

    file_path = os.path.join("uploads", filename)
    file.save(file_path)

    download_token = generate_encrypted_url(filename)

    new_file = File(
        file_name=filename,
        file_type=ext,
        file_path=file_path,
        uploaded_by=user.id,
        download_token=download_token
    )

    db.session.add(new_file)
    db.session.commit()

    return jsonify(msg="File uploaded", download_link=f"/client/download/{download_token}"), 201

    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user.role != 'Ops':
        return jsonify(msg="Unauthorized"), 403

    file = request.files['file']
    filename = secure_filename(file.filename)
    ext = filename.rsplit('.', 1)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        return jsonify(msg="Invalid file type"), 400

    file_path = os.path.join("uploads", filename)
    file.save(file_path)

    download_token = generate_encrypted_url(filename)

    new_file = File(file_name=filename, file_type=ext, file_path=file_path, uploaded_by=user_id, download_token=download_token)
    db.session.add(new_file)
    db.session.commit()

    return jsonify(msg="File uploaded", download_link=f"/client/download/{download_token}"), 201
