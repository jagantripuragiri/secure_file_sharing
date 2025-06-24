from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_cors import CORS

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
mail = Mail()  # 👈 Add this

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'

    # Mail config
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
    app.config['MAIL_PASSWORD'] = 'your_password'
    app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)  # 👈 Don't forget this
    CORS(app)

    from app.routes.ops_routes import ops_bp
    from app.routes.client_routes import client_bp

    app.register_blueprint(ops_bp, url_prefix='/ops')
    app.register_blueprint(client_bp, url_prefix='/client')

    return app
