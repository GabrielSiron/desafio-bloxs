from .. import db

from app.models.base_class import BaseClass
from app.models.person import Person

class Account(db.Model, BaseClass):
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(120))
    amount = db.Column(db.Float, default=0)
    is_active = db.Column(db.Boolean, default=True)
    person_id = db.Column(db.ForeignKey('person.id'), nullable=False)
    person = db.relationship('Person', foreign_keys=person_id, order_by='Person.id')
    account_type_id = db.Column(db.ForeignKey('account_type.id'), nullable=False)
    account_type = db.relationship('AccountType', foreign_keys=account_type_id, order_by='AccountType.id')

    def __str__(self):
        return str(self.name) + str(self.id)

    @classmethod
    def cpf_already_registered(cls, cpf):
        from app.database import DataBaseConnection

        account = DataBaseConnection.select_one(Person, {"cpf": cpf})
        return account is not None

    @classmethod
    def find_account_by_email(cls, email):
        from app.database import DataBaseConnection

        account = DataBaseConnection.select_one(Account, {"email": email})
        return account
    
    @classmethod
    def find_account_by_id(cls, id):
        from app.database import DataBaseConnection

        account = DataBaseConnection.select_one(Account, {"id": id})
        return account
    
    @classmethod
    def email_already_registered(cls, email):
        account = cls.find_account_by_email(email)
        return account is not None

    @classmethod
    def change_amount(cls, transaction_value, account_id):
        from sqlalchemy.orm.attributes import flag_modified

        account = cls.find_account_by_id(account_id)
        account = Account(**account)
        account.amount += transaction_value
        
        flag_modified(account, 'amount')
        db.session.merge(account)
        db.session.flush()
        db.session.commit()

        return account

    @classmethod
    def block_account(cls, account_id):
        from sqlalchemy.orm.attributes import flag_modified

        account = cls.find_account_by_id(account_id)
        account = Account(**account)
        account.is_active = False

        flag_modified(account, 'is_active')
        db.session.merge(account)
        db.session.flush()
        db.session.commit()

        return account

    def to_json(self):
        return {
            "email": self.email,
            "amount": self.amount
        }