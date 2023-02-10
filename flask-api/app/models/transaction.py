from .. import db

from app.models.base_class import BaseClass

class Transaction(db.Model, BaseClass):
    value = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    transfer_sender_id = db.Column(db.ForeignKey('account.id'))
    transfer_sender = db.relationship('Account', foreign_keys=transfer_sender_id, order_by='Account.id')
    transfer_receiver_id = db.Column(db.ForeignKey('account.id'))
    transfer_receiver = db.relationship('Account', foreign_keys=transfer_receiver_id, order_by='Account.id')
    
    @classmethod
    def get_transactions(cls, account_id):
        from app.database import DataBaseConnection
        last_transferences = DataBaseConnection.select_transactions(account_id)

        return last_transferences
    
    @classmethod
    def get_sent_transactions_amount(cls, account_id):
        from app.database import DataBaseConnection
        from datetime import datetime

        date, full_time = str(datetime.now()).split()
        time_without_zone = full_time.split('.')[0]

        today = date + 'T' + time_without_zone
        print(today)

        filter = { 
            'transfer_sender_id': account_id,
            'transaction_date': date
        }

        transferences = DataBaseConnection.select_many(Transaction, filter)

        total = 0
        for transference in transferences:
            print("Tr: ", transference)
            total += transference[3]
        
        return total

    def to_json(self):
        return {
            'value': self.value,
            'transaction_date': self.transaction_date,
            'account_id': self.account_id
        }