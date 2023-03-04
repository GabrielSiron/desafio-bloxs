from app.authentication import Authentication

from app.utils import get_current_user
from app.utils import transaction_mapping

from app.models.transaction import Transaction

from flask import jsonify

def define_transaction_routes(app, db):
    @app.route('/transactions/<int:page>', methods=['GET'])
    def get_transactions(page):
        
        account_id = get_current_user()
        transactions = Transaction.get_transactions(page, account_id)
        
        return jsonify(
            {
                'message': 'ok', 
                'transactions': transactions
            }
        ), 200

    @app.route('/transaction', methods=['POST'])
    def create_transaction():
        transfer_sender_id = request.json['transfer_sender_id']
        transfer_receiver_id = request.json['transfer_receiver_id']
        value = request.json['value']
        
        account_id = Authentication.find_id_by_token(token)
        
        if account_id == transfer_sender_id:

            amount = Transaction.get_sent_transactions_amount(account_id)
            account = Account.find_account_by_id(account_id)
            
            account_type = AccountType.find_account_type_by_id(account[account_mapping['account_type_id']])

            if account[account_mapping['is_active']] == False:
                return jsonify(
                    {
                        'message': 'Conta bloqueada. Você não pode realizar saques.'
                    }
                ), 400

            if amount + value > account_type[account_type_mapping['drawing_limit']]:
                name = account_type[account_type_mapping['name']]
                limit = account_type[account_type_mapping['drawing_limit']]
                
                return jsonify(
                    {
                        'message': f'Limite de saque excedido. O seu tipo de conta ({ name }) permite um limite diário de R$ { limit }'
                    }
                ), 400  
        
        transaction = Transaction(**request.json)
        
        db.session.add_all([transaction])
        db.session.commit()

        if transfer_sender_id:
            changed_account_sender = Account.change_amount(-transaction.value, transfer_sender_id)
            return jsonify(
                {
                    'message': 'ok',
                    'account': changed_account_sender.to_json()
                }
            ), 200

        if transfer_receiver_id:
            Account.change_amount(transaction.value, transfer_receiver_id)
            return jsonify(
                {
                    'message': 'ok'
                }
            )
