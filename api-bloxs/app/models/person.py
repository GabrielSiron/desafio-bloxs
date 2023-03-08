from .. import db

from app.models.base_class import BaseClass

class Person(db.Model, BaseClass):
    name = db.Column(db.String(30), nullable=False)
    cpf = db.Column(db.String(15), unique=True)
    birth_date = db.Column(db.DateTime)

    @classmethod
    def find_person_by_id(cls, id):

        query = "SELECT * FROM account WHERE id='" + str(id) + "'"
        person_tuple = db.session.execute(query).first()

        if person_tuple:
            
            person_dict = {
                'id': person_tuple[0],
                'created_at': person_tuple[1],
                'updated_at': person_tuple[2],
                'name': person_tuple[3],
                'cpf': person_tuple[4],
                'birth_date': person_tuple[5]
            }

            return Person(**person_dict)
            