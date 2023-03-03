

def get_form_items_to_registry(request):
    return request.json['cpf'], request.json['email'], request.json['name'], request.json['birth'], request.json['password']

def get_form_items_to_login(request):
    return request.json['email'], request.json['password']

def generate_account_object(request):
    from app.models.account_type import AccountType
    from app.models.account import Account
    from app.models.person import Person
    from app.database import DataBaseConnection
    from app.models.account import Account

    cpf, email, name, birth_date, password = get_form_items_to_registry(request)
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

    return new_account

def get_user_by_auth_token(request):
    from app.authentication import Authentication
    
    token = request.headers['token']
    account_id = Authentication.find_id_by_token(token)
    return account_id

account_mapping = {
    'id': 0,
    'created_at': 1,
    'updated_at': 2,
    'email': 3,
    'password': 4,
    'amount': 5,
    'is_active': 6,
    'person_id': 7,
    'account_type_id': 8
}

person_mapping = {
    'id': 0,
    'created_at': 1,
    'updated_at': 2,
    'name': 3,
    'cpf': 4,
    'birth_date': 5
}

transaction_mapping = {
    'id': 0,
    'created_at': 1,
    'updated_at': 2,
    'value': 3,
    'transaction_date': 4,
    'transfer_sender_id': 5,
    'transfer_receiver_id': 6
}

account_type_mapping = {
    'id': 0,
    'created_at': 1,
    'updated_at': 2,
    'name': 3,
    'drawing_limit': 4
}