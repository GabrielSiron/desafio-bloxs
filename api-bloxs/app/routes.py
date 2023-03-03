from . import create_app
from . import db

from .models.account import Account
from .models.person import Person
from .models.account_type import AccountType
from .models.transaction import Transaction

from .database import DataBaseConnection
from .authentication import Authentication

from .utils import get_form_items_to_registry, generate_account_object
from .utils import get_form_items_to_login, get_user_by_auth_token

from .utils import account_mapping, person_mapping, transaction_mapping, account_type_mapping

from flask_cors import CORS

import os
import bcrypt
import pymysql

from flask import jsonify, request

from werkzeug.security import generate_password_hash

app = create_app()

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

with app.app_context():
    db.create_all()

@app.route('/signup', methods=['POST'])
def create_account():
    cpf, email, name, birth_date, password = get_form_items_to_registry(request)

    if Account.cpf_already_registered(cpf):
        return jsonify({"message": "cpf já cadastrado"}), 401

    if Account.email_already_registered(email):
        return jsonify({"message": "email já registrado"}), 402

    account = generate_account_object(request)

    db.session.add_all([account])
    db.session.commit()

    return jsonify(account.to_json()), 200

@app.route('/signin', methods=['POST'])
def initialize_session():

    email, password = get_form_items_to_login(request)
    account = Account.find_account_by_email(email)

    if account is not None:
        if account.password == password:
            token = Authentication.generate_token(request)
            Authentication.create_session(token, account.id)

            return jsonify(
                {   
                    "message": "Sessão iniciada!",
                    "user": {
                        "email": account.email,
                        "id": account.id,
                        "token": token.decode()
                    }
                }
            ), 200

        else:
            return jsonify({"message": "Email ou senha incorretos"}), 400
    else:
        return jsonify({"message": "Email ou senha incorretos"}), 400

@app.route('/transactions/<int:page>', methods=['GET'])
def get_transactions(page):
    account_id = get_user_by_auth_token(request)
    transactions = Transaction.get_transactions(page, account_id)
    
    return jsonify(
        {
            'message': 'ok', 
            'transactions': [
                {
                    'value': transaction[transaction_mapping['value']], 
                    'date': transaction[transaction_mapping['transaction_date']],
                    'tranfer_sender_id': transaction[transaction_mapping['transfer_sender_id']],
                    'tranfer_receiver_id': transaction[transaction_mapping['transfer_receiver_id']],
                    'is_sender': account_id == transaction[transaction_mapping['transfer_sender_id']]
                } for transaction in transactions]
        }
    ), 200

@app.route('/transaction', methods=['POST'])
def create_transaction():
    token = request.headers.get('token', None)
    if token and Authentication.is_authenticated(token):
        transfer_sender_id = request.json['transfer_sender_id']
        transfer_receiver_id = request.json['transfer_receiver_id']
        value = int(request.json['value'])
        
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
    
    return jsonify(
        {
            'message': 'Não autorizado, faça login'
        }
    ), 403
    
    

@app.route('/account', methods=['GET'])
def get_account():

    token = request.headers.get('token', None)
    if token and Authentication.is_authenticated(token):
        account_id = Authentication.find_id_by_token(token)
        account = Account.find_account_by_id(account_id)
        person_id = account[account_mapping['person_id']]
        person = Person.find_person_by_id(person_id)

        return jsonify(
            {
                'message': 'ok',
                'amount': account[account_mapping['amount']],
                'name': person[person_mapping['name']],
                'cpf': person[person_mapping['cpf']],
                'email': account[account_mapping['email']],
                'id': account[account_mapping['id']]
            }
        ), 200
    
    return jsonify(
        {
            'message': 'Não autorizado, faça login'
        }
    ), 403


@app.route('/block', methods=['PUT'])
def block_account():
    token = request.headers.get('token', None)
    if token and Authentication.is_authenticated(token):
        account_id = Authentication.find_id_by_token(token)
        Account.block_account(account_id)

        return jsonify(
            {
                'message': 'Conta Bloqueada com sucesso!'
            }
        )

    return jsonify(
        {
            'message': 'Não autorizado, faça login'
        }
    ), 403

app.run()