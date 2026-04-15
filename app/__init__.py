from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

import os

def create_app():
    
    app = Flask(__name__,
                template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), "app/templates"),
                static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), "app/static"))
    app.config.from_object("config.config")
    
    db.init_app(app)
    from .contactos.routes import contactos_bp
    app.register_blueprint(contactos_bp)
    

    
    return app