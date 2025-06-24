from app import db
from datetime import datetime

from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # ✅ Required
    role = db.Column(db.String(10), nullable=False)        # 'ops' or 'client'
    verified = db.Column(db.Boolean, default=False)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(200), nullable=False)
    file_type = db.Column(db.String(10), nullable=False)
    file_path = db.Column(db.String(300), nullable=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    download_token = db.Column(db.String(256), nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
