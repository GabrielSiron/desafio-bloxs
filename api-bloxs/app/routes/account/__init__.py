from app.authentication import Authentication

from app.models.account import Account
from app.models.person import Person

from flask import request, jsonify

def define_account_routes(app, db):
    @app.route('/account', methods=['GET'])
    def get_account():
        
        token = request.headers['token'] or ''
        account_id = Authentication.find_id_by_token(token)
        account = Account.find_by('id', account_id)
        person_id = account.person_id
        person = Person.find_person_by_id(person_id)

        return jsonify(
            {
                'message': 'ok',
                'amount': account.amount,
                'name': person.name,
                'cpf': person.cpf,
                'email': account.email,
                'id': account.id
            }
        ), 200

    @app.route('/block', methods=['PUT'])
    def block_account():
        token = request.headers['token'] or ''
        account_id = Authentication.find_id_by_token(token)
        Account.block_account(account_id)

        return jsonify(
            {
                'message': 'Conta Bloqueada com sucesso!'
            }
        )
