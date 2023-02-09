import os

from flask import jsonify, request
import bcrypt
from werkzeug.security import generate_password_hash

from . import create_app
from . import db

from .models.account import Account
from .models.person import Person
from .models.account_type import AccountType
from .models.transaction import Transaction

from .authentication import Authentication
from flask_cors import CORS

from .database import DataBaseConnection

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

app.app_context().push()
CORS(app)

db.create_all()

@app.route('/')
def index():
    return jsonify({"message": "Olá, Mundo!"})

@app.route('/signup', methods=['POST'])
def create_account():
    cpf = request.json['cpf']
    email = request.json['email']
    name = request.json['name']
    birth_date = request.json['birth']
    password = request.json['password']

    if Account.cpf_already_registered(cpf):
        return jsonify(
            {
                "message": "cpf já cadastrado"
            }
        ), 401

    if Account.email_already_registered(email):
        return jsonify(
            {
                "message": "email já registrado"
            }
        ), 402
    
    account_type = DataBaseConnection.select_one(AccountType, { 'name': 'Conta Fácil' })

    person_json = {
        'name': name,
        'cpf': cpf,
        'birth_date': birth_date
    }

    account_json = {
        'email': email,
        'password': password,
        'account_type_id': account_type[0]
    }

    
    new_account = Account(**account_json)
    new_account.person = Person(**person_json)
    db.session.add_all([new_account])
    db.session.commit()

    return jsonify(new_account.to_json()), 200

@app.route('/signin', methods=['POST'])
def initialize_session():

    email = request.json['email']
    password = request.json['password']
    
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
    token = request.headers['token']
    account_id = Authentication.find_id_by_token(token)
    print("configs", account_id)
    transactions = Transaction.get_transactions(page, account_id)
    

    return jsonify(
        {
            'message': 'ok', 
            'transactions': [
                {
                    'value': transaction[3], 
                    'date': transaction[4],
                    'tranfer_sender_id': transaction[5],
                    'tranfer_receiver_id': transaction[6],
                    'is_sender': account_id == transaction[5]
                } for transaction in transactions]
        }
    ), 200

@app.route('/transaction', methods=['POST'])
def create_transaction():
    transfer_sender_id = request.json['transfer_sender_id']
    transfer_receiver_id = request.json['transfer_receiver_id']
    transaction = Transaction(**request.json)
    db.session.add_all([transaction])
    db.session.commit()
    
    changed_account_sender = Account.change_amount(-transaction.value, transfer_sender_id)
    Account.change_amount(transaction.value, transfer_receiver_id)
    
    return jsonify(
        {
            'message': 'ok',
            'account': changed_account_sender.to_json()
        }
    ), 200

@app.route('/account', methods=['GET'])
def get_account():
    token = request.headers['token']
    account_id = Authentication.find_id_by_token(token)
    account = Account.find_account_by_id(account_id)
    return jsonify(
        {
            'message': 'ok',
            'amount': account[5],
            # 'name': account[4],
            'id': account[0]
        }
    ), 200

app.run()