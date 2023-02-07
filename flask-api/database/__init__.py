from models.account import Account 
from models.account_type import AccountType
from models.transaction import Transaction
from models.person import Person

from sqlalchemy import create_engine

from sqlalchemy import Integer, String, Boolean, DateTime, Float
from sqlalchemy import MetaData, ForeignKey, Table, Column

class Builder:

    engine = create_engine("mysql+pymysql://gabriel:143867@0.0.0.0:3306/mysql")
    metadata = MetaData(engine)
    classes = [Account, AccountType, Transaction, Person]

    @classmethod
    def define_tables(cls):
        
        account = Table(
            'Account', cls.metadata,
                Column('id', Integer, primary_key=True),
                Column('email', String(40), unique=True),
                Column('password', String(50)),
                Column('amount', Float),
                Column('person_id', ForeignKey('Person.id'), nullable=False),
                Column('account_type_id', ForeignKey('AccountType.id'), nullable=False)
        )

        account_type = Table(
            'AccountType', cls.metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String(40), primary_key=True),
                Column('drawing_limit', Float, primary_key=True),
        )

        person = Table(
            'Person', cls.metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String(40), unique=True),
                Column('cpf', String(11)),
                Column('birth_date', DateTime)
        )

        transaction = Table(
            'Transaction', cls.metadata,
                Column('id', Integer, primary_key=True),
                Column('date', DateTime, primary_key=True),
                Column('account_id', ForeignKey('Account.id'), nullable=False)
        )


    @classmethod
    def create_schema(cls):
        cls.metadata.create_all()