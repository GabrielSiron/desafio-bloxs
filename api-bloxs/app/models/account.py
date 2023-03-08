"""Account File"""

from app.models.base_class import BaseClass

from sqlalchemy.orm.attributes import flag_modified

from .. import db

class Account(db.Model, BaseClass):
    """Account Class"""
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
        """Verifica se o CPF passado já foi registrado em banco"""
        
        account = cls.find_by('cpf', cpf)
        return account is not None
    
    @classmethod
    def email_already_registered(cls, email):
        
        account = cls.find_by('email', email)
        return account is not None

    @classmethod
    def change_amount(cls, transaction_value, account_id):

        account = cls.find_by('id', account_id)
        account.amount += transaction_value

        flag_modified(account, 'amount')
        db.session.merge(account)
        db.session.flush()
        db.session.commit()

        return account

    @classmethod
    def block_account(cls, account_id):
        
        account = cls.find_by('id', account_id)
        account = Account(**account)
        account.is_active = False

        flag_modified(account, 'is_active')
        db.session.merge(account)
        db.session.flush()
        db.session.commit()

        return account

    @staticmethod
    def find_by(attribute, value):
        query = "SELECT * FROM account WHERE " + str(attribute) + "='" + str(value) + "'"
        account_tuple = db.session.execute(query).first()

        if account_tuple:
            
            account_dict = {
                'id': account_tuple[0],
                'created_at': account_tuple[1],
                'updated_at': account_tuple[2],
                'email': account_tuple[3],
                'password': account_tuple[4],
                'amount': account_tuple[5],
                'is_active': account_tuple[6],
                'person_id': account_tuple[7],
                'account_type_id': account_tuple[8]
            }

            return Account(**account_dict)
        
    def to_json(self):
        return {
            "email": self.email,
            "amount": self.amount
        }