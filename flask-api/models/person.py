from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.base_class import BaseClass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gabriel:143867@localhost/db?host=localhost?port=8080'
db = SQLAlchemy(app)

class Person(db.Model, BaseClass):
    name = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, nullable=False, unique=True)
    date_of_birth = db.Column(db.DateTime)
