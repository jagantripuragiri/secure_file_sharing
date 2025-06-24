from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)

    # Import and register your blueprints
    from app.routes.ops_routes import ops_bp
    from app.routes.client_routes import client_bp

    app.register_blueprint(ops_bp, url_prefix='/api/ops')
    app.register_blueprint(client_bp, url_prefix='/api/client')

    return app
