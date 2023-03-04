from app.utils import (get_signup_form, get_missing_fields, generate_account_object,
                        get_signin_form)

from app.handling_error import Error
from app.models.account import Account

from app.authentication import Authentication

from flask import jsonify, request

def define_auth_routes(app, db):

    @app.route('/signup', methods=['POST'])
    def create_account():
        missing_fields = get_missing_fields(['cpf', 'email', 'name', 'birth', 'password'])

        if len(missing_fields) != 0:
            error = "Formulário incompleto. Os seguintes campos não foram enviados:\n -" + '\n - '.join(missing_fields)

            return jsonify({"message": error}), 400

        cpf, email, name, birth_date, password = get_signup_form()
        account = generate_account_object()

        try:
            db.session.add_all([account])
            db.session.commit()
        
        except Exception as e:
            
            error = Error(e)
            message = error.handle_sqlalchemy_errors()

            return jsonify({ "message" : message }), 400

        return jsonify(account.to_json()), 200
    
    @app.route('/signin', methods=['POST'])
    def initialize_session():
        missing_fields = get_missing_fields(['email', 'password'])
        
        if len(missing_fields) != 0:
            error = "Formulário incompleto. Os seguintes campos não foram enviados:\n -" + '\n - '.join(missing_fields)

        email, password = get_signin_form()
        account = Account.find_account_by_email(email)

        if account and account.password == password:
            token = Authentication.generate_token(request).decode()
            Authentication.create_session(token, account.id)

            return jsonify(
                {   
                    "message": "Sessão iniciada!",
                    "user": {
                        "email": account.email,
                        "id": account.id,
                        "token": token
                    }
                }
            ), 200

        else:
            return jsonify({"message": "Email ou senha incorretos"}), 400