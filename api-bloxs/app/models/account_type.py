"""AccountType File"""

from app.database import DataBaseConnection
from app.models.base_class import BaseClass

from .. import db

class AccountType(db.Model, BaseClass):
    """AccountType Class"""
    name = db.Column(db.String(30), nullable=False, unique=True)
    drawing_limit = db.Column(db.Float, nullable=False)

    @classmethod
    def find_account_type_by_id(cls, id):
        """Procura pelo id e retorna objeto contendo dados de account_type"""

        account_type = DataBaseConnection.select_one(AccountType, {"id": id})
        return account_type
