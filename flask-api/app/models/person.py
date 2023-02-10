from .. import db

from app.models.base_class import BaseClass

class Person(db.Model, BaseClass):
    name = db.Column(db.String(30), nullable=False)
    cpf = db.Column(db.String(15), unique=True)
    birth_date = db.Column(db.DateTime)