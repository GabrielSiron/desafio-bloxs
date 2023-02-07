from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.base_class import BaseClass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gabriel:143867@localhost/db?host=localhost?port=8080'
db = SQLAlchemy(app)

class Account(db.Model, BaseClass):
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    amount = db.Column(db.Integer)
    person_id = db.Column(db.ForeignKey('person.id'), nullable=False)
    person = db.relationship('Person', foreign_keys=person_id, order_by='Person.id')

    