from .. import db

from app.models.base_class import BaseClass

from datetime import datetime

class Transaction(db.Model, BaseClass):
    value = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False, default=db.func.now())
    transfer_sender_id = db.Column(db.ForeignKey('account.id'))
    transfer_sender = db.relationship('Account', foreign_keys=transfer_sender_id, order_by='Account.id')
    transfer_receiver_id = db.Column(db.ForeignKey('account.id'))
    transfer_receiver = db.relationship('Account', foreign_keys=transfer_receiver_id, order_by='Account.id')
    
    @classmethod
    def get_transactions(cls, page, account_id):
        results_per_page = 10
        account_condiction = f"transfer_sender_id = {str(account_id)}"
        query = f"SELECT * FROM transaction WHERE {account_condiction} LIMIT {page*results_per_page},{results_per_page}"

        query_result = db.session.execute(query).all()
        transactions = cls.convert_in_transaction(query_result)

        for index, transaction in enumerate(transactions):
            transactions[index] = transaction.to_json(account_id)

        return transactions

    @classmethod
    def get_transactions_of_today(cls, account_id):
        
        date, _ = str(datetime.now()).split()
        
        min_date = date + "T00:00:00"
        max_date = date + 'T23:59:59'

        min_condiction = f"transaction_date >= '{str(min_date)}'"
        max_condiction = f"transaction_date <= '{str(max_date)}'"
        sender_condiction = f"transfer_sender_id = {str(account_id)}"

        query = f"SELECT * FROM transaction WHERE {min_condiction} AND {max_condiction} AND {sender_condiction}"
        
        query_result = db.session.execute(query).all()

        transactions = cls.convert_in_transaction(query_result)

        total = 0
        for transaction in transactions:
            total += transaction.value
        
        return total

    def convert_in_transaction(transactions):

        converted_transactions = []
        for transaction_tuple in transactions:
            if transaction_tuple:
                
                transaction_dict = {
                    'id': transaction_tuple[0],
                    'created_at': transaction_tuple[1],
                    'updated_at': transaction_tuple[2],
                    'value': transaction_tuple[3],
                    'transaction_date': transaction_tuple[4],
                    'transfer_sender_id': transaction_tuple[5],
                    'transfer_receiver_id': transaction_tuple[6]
                }

                converted_transactions.append(Transaction(**transaction_dict))
        return converted_transactions

    def to_json(self, account_id):
        return {
            'value': self.value,
            'transaction_date': self.transaction_date,
            'tranfer_sender_id': self.transfer_sender_id,
            'tranfer_receiver_id': self.transfer_receiver_id,
            'is_sender': self.transfer_sender_id == account_id
        }
    
    
