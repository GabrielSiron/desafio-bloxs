"""AccountType File"""
from app.models.base_class import BaseClass

from .. import db

class AccountType(db.Model, BaseClass):
    """AccountType Class"""
    name = db.Column(db.String(30), nullable=False, unique=True)
    drawing_limit = db.Column(db.Float, nullable=False)

    @classmethod
    def find_account_type_by_id(cls, id):
        """Procura pelo id e retorna objeto contendo dados de account_type"""
        account_type = cls.filtering("SELECT * FROM account_type WHERE id='" + str(id) + "'")
        
        return account_type

    @staticmethod
    def filtering(query):
        account_type_tuple = db.session.execute(query).first()

        if account_type_tuple:
            
            account_type_dict = {
                'id': account_type_tuple[0],
                'created_at': account_type_tuple[1],
                'updated_at': account_type_tuple[2],
                'name': account_type_tuple[3],
                'drawing_limit': account_type_tuple[4]
            }

            return AccountType(**account_type_dict)
