from app.utils import get_signup_form, get_missing_fields, generate_account_object
from flask import jsonify, request

def define_auth_routes(app, db):

    @app.route('/signup', methods=['POST'])
    def create_account():
        missing_fields = get_missing_fields()

        if len(missing_fields) != 0:
            error = "Formulário incompleto. Os seguintes campos não foram enviados:\n -" + '\n - '.join(missing_fields)

            return jsonify(
                {
                    "message": error
                }
            )

        form = get_signup_form()

        cpf, email, name, birth_date, password = form

        # if Account.cpf_already_registered(cpf):
        #     return jsonify({"message": "cpf já cadastrado"}), 401

        # if Account.email_already_registered(email):
        #     return jsonify({"message": "email já registrado"}), 402

        account = generate_account_object()

        try:
            db.session.add_all([account])
            db.session.commit()
        
        except Exception as e:
            print(e)
            return jsonify(
                {
                    "message": str(e)
                }
            )
        return jsonify(account.to_json()), 200