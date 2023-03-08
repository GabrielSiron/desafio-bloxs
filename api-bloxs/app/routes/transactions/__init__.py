"""Rotas de Transação"""

from app.authentication import Authentication

from app.utils import get_current_user_id

from app.models.transaction import Transaction
from app.models.account import Account
from app.models.account_type import AccountType

from flask import jsonify, request

def define_transaction_routes(app, db):
    """Define funções para rotas de Transação"""

    @app.route('/transactions/', methods=['GET'])
    def get_transactions():

        page: int = int(request.args.get('page'))
        account_id: int = get_current_user_id()
        transactions: list = Transaction.get_transactions(page, account_id)

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
        token = request.headers['token']
        account_id = Authentication.find_id_by_token(token)
        account = Account.find_by('id', account_id)

        if account_is_active(account):
            return jsonify({'message': 'Conta bloqueada. Você não pode realizar transações.'}), 400

        if user_is_sender():

            amount = Transaction.get_transactions_of_today(account_id)
            account_type = AccountType.find_account_type_by_id(account.account_type_id)

            if transaction_breaks_limit(amount, value, account_type):
                message = generate_error_message(account_type)

                return jsonify(
                    {
                        'message': message
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

        else:
            Account.change_amount(transaction.value, transfer_receiver_id)
            return jsonify(
                {
                    'message': 'ok'
                }
            )

def transaction_breaks_limit(amount, value_of_transaction, account_type):
    """Verifica se a transação atual vai ultrapassar o limite da conta do usúário"""
    return amount + value_of_transaction > account_type.drawing_limit

def account_is_active(account):
    """Verifica se a conta passada está ativa"""
    return account.is_active is False

def generate_error_message(account_type):
    """Gera mensagem de erro para limite de saque excedido"""
    name = account_type.name
    limit = account_type.drawing_limit
    message = f'Limite excedido. A ({ name }) permite um limite diário de R$ { limit }'
    return message

def user_is_sender():
    "Verifica se o usuário atual está mandando o valor para outra conta"
    transfer_sender_id = request.json['transfer_sender_id']
    token = request.headers['token']
    account_id = Authentication.find_id_by_token(token)
    return account_id == transfer_sender_id