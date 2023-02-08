import os

from flask import jsonify, request
import bcrypt
from werkzeug.security import generate_password_hash

from . import create_app
from . import db

from .models.account import Account
from .models.account_type import AccountType
from .models.transaction import Transaction

from .authentication import Authentication

from .database import DataBaseConnection

auth = Authentication()
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

app.app_context().push()

db.create_all()

@app.route('/')
def index():
    return jsonify({"message": "Olá, Mundo!"})

@app.route('/signup', methods=['POST'])
def create_account():
    cpf = request.json['cpf']
    email = request.json['email']

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


    new_account = Account(**request.json)  
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
            token = auth.generate_token(request)

            return jsonify(
                {   
                    "message": "Sessão iniciada!",
                    "user": {
                        "name": account.name,
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
    transactions = Transaction.get_transactions(page)

    return jsonify(
        {
            'message': 'ok', 
            'transactions': [transaction.to_json() for transaction in transactions]
        }
    ), 200

@app.route('/transaction', methods=['POST'])
def create_transaction():
    account_id = request.json['account_id']
    transaction = Transaction(**request.json)
    db.session.add_all([transaction])
    db.session.commit()
    
    changed_account = Account.change_amount(transaction.value, account_id)
    
    return jsonify(
        {
            'message': 'ok',
            'account': changed_account.to_json()
        }
    ), 200

app.run()