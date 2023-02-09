from .. import db

from app.models.base_class import BaseClass

class Transaction(db.Model, BaseClass):
    value = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    transfer_sender_id = db.Column(db.ForeignKey('account.id'), nullable=False)
    transfer_sender = db.relationship('Account', foreign_keys=transfer_sender_id, order_by='Account.id')
    transfer_receiver_id = db.Column(db.ForeignKey('account.id'), nullable=False)
    transfer_receiver = db.relationship('Account', foreign_keys=transfer_receiver_id, order_by='Account.id')
    
    @classmethod
    def get_transactions(cls, page, account_id):
        from app.database import DataBaseConnection

        sender_transfereces = DataBaseConnection.select_many(Transaction, { 'transfer_sender_id': account_id })

        # receiver_transfereces = DataBaseConnection.select_many(Transaction, { 'transfer_receiver_id': account_id })
        return sender_transfereces
    
    def to_json(self):
        return {
            'value': self.value,
            'transaction_date': self.transaction_date,
            'account_id': self.account_id
        }