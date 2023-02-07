from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.Integer)
    amount = db.Column(db.Integer)

    