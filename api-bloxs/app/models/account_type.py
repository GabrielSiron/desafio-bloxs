from .. import db

from app.models.base_class import BaseClass

class AccountType(db.Model, BaseClass):
    name = db.Column(db.String(30), nullable=False, unique=True)
    drawing_limit = db.Column(db.Float, nullable=False)

    @classmethod
    def find_account_type_by_id(cls, id):
        from app.database import DataBaseConnection

        account_type = DataBaseConnection.select_one(AccountType, {"id": id})
        return account_type
