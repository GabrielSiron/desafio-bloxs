import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = None

def create_app():
    global migrate

    app = Flask(__name__)
    migrate = Migrate(app, db)
    
    config_name = os.getenv('FLASK_CONFIG') or 'default'

    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gabriel:143867@0.0.0.0:3306/mysql'
    app.config['SECRET_KEY'] = 'akd3n13nf9canjfj6khvn'
    
    config[config_name].init_app(app)
    
    db.init_app(app)
    migrate.init_app(app)

    return app