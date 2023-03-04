from .. import db

from app.utils import transaction_mapping
from app.models.base_class import BaseClass

class Transaction(db.Model, BaseClass):
    value = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False, default=db.func.now())
    transfer_sender_id = db.Column(db.ForeignKey('account.id'))
    transfer_sender = db.relationship('Account', foreign_keys=transfer_sender_id, order_by='Account.id')
    transfer_receiver_id = db.Column(db.ForeignKey('account.id'))
    transfer_receiver = db.relationship('Account', foreign_keys=transfer_receiver_id, order_by='Account.id')
    
    @classmethod
    def get_transactions(cls, page, account_id):
        from app.database import DataBaseConnection
        transactions = DataBaseConnection.select_transactions(page, account_id)

        transactions = [
            {
                'value': transaction[transaction_mapping['value']], 
                'date': transaction[transaction_mapping['transaction_date']],
                'tranfer_sender_id': transaction[transaction_mapping['transfer_sender_id']],
                'tranfer_receiver_id': transaction[transaction_mapping['transfer_receiver_id']],
                'is_sender': account_id == transaction[transaction_mapping['transfer_sender_id']]
            } for transaction in transactions]

        return transactions
    
    @classmethod
    def get_sent_transactions_amount(cls, account_id):
        from app.database import DataBaseConnection

        transactions = DataBaseConnection.select_transactions_of_today(account_id)

        total = 0
        for transference in transactions:
            print("Tr: ", transference)
            total += transference[3]
        
        return total

    def to_json(self):
        return {
            'value': self.value,
            'transaction_date': self.transaction_date,
            'account_id': self.account_id
        }