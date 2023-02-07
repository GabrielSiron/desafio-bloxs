from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.base_class import BaseClass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gabriel:143867@localhost/db?host=localhost?port=8080'
db = SQLAlchemy(app)

class AccountType(db.Model, BaseClass):
    name = db.Column(db.String, nullable=False, unique=True)
    drawing_limit = db.Column(db.Float, nullable=False)

