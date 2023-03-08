"""Funções e objetos úteis"""

from app.authentication import Authentication

from app.models.account import Account
from app.models.account_type import AccountType
from app.models.person import Person

from app import db



from flask import request

def get_signup_form():
    """Retorna uma tupla com as informações de formulário de cadastro"""
    form = []
    form.append(request.json['cpf'])
    form.append(request.json['email'])
    form.append(request.json['name'])
    form.append(request.json['birth'])
    form.append(request.json['password'])
    return form

def get_signin_form():
    """Retorna uma tupla com as informações de formulário de login"""
    return request.json['email'], request.json['password']

def create_account_object():
    """Retorna um objeto do tipo Account do usuário atual"""
    cpf, email, name, birth_date, password = get_signup_form()
    
    name_condiction = "name = 'Conta Fácil'"
    query = f"SELECT * FROM account_type WHERE {name_condiction}"

    account_type = db.session.execute(query).first()
    
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

    return new_account

def get_current_user_id():
    """Retona o id do usuário atual"""
    
    token = request.headers['token']
    account_id = int(Authentication.find_id_by_token(token))
    return account_id

def get_missing_fields(list_of_fields=None):
    """Retorna o nome dos campos faltantes na submissão de um formulário"""
    missing_fields = []
    for field in list_of_fields:
        if not request.json.get(field):
            missing_fields.append(field)
    
    return missing_fields
