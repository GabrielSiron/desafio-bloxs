from .. import db

from app.models.base_class import BaseClass

class Account(db.Model, BaseClass):
    name = db.Column(db.String(30), nullable=False)
    cpf = db.Column(db.String(15))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(40))
    amount = db.Column(db.Integer)


    