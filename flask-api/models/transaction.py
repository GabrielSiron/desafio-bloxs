from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.base_class import BaseClass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gabriel:143867@localhost/db?host=localhost?port=8080'
db = SQLAlchemy(app)

class Transaction(db.Model, BaseClass):
    value = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    account_id = db.Column(db.ForeignKey('account.id'), nullable=False)
    account = db.relationship('Account', foreign_keys=account_id, order_by='Account.id')