import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    print(os.getenv("DEV_DATABASE_URL"))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gabriel:143867@0.0.0.0:3306/mysql'
    config[config_name].init_app(app)

    db.init_app(app)
    return app