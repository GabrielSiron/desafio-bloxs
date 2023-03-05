from app.authentication import Authentication

from app.models.account import Account
from app.models.person import Person

from app.utils import account_mapping, person_mapping

from flask import request, jsonify

def define_account_routes(app, db):
    @app.route('/account', methods=['GET'])
    def get_account():
        
        token = request.headers['token']
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

    @app.route('/block', methods=['PUT'])
    def block_account():
        token = request.headers['token']
        account_id = Authentication.find_id_by_token(token)
        Account.block_account(account_id)

        return jsonify(
            {
                'message': 'Conta Bloqueada com sucesso!'
            }
        )
