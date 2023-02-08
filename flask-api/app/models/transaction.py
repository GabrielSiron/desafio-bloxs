from .. import db

from app.models.base_class import BaseClass

class Transaction(db.Model, BaseClass):
    value = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    account_id = db.Column(db.ForeignKey('account.id'), nullable=False)
    account = db.relationship('Account', foreign_keys=account_id, order_by='Account.id')
    
    @classmethod
    def get_transactions(cls, page):

        transactions = cls.query.paginate(page=page, per_page=1)
        print(transactions)

        return transactions
    
    def to_json(self):
        return {
            'value': self.value,
            'transaction_date': self.transaction_date,
            'account_id': self.account_id
        }