import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    
    environment = os.getenv('ENV', 'DEV')

    if environment == 'DEV':
        app.config['DEBUG'] = True
        app.config['ENV'] = 'development'
    elif environment == 'PRO':
        app.config['DEBUG'] = False
        app.config['ENV'] = 'production'

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
