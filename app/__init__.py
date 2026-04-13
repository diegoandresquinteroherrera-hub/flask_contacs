from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    app.config.from_object("config.config")
    
    db.init_app(app)
    from .contactos.routes import contactos_bp
    app.register_blueprint(contactos_bp)
    
    return app