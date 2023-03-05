"""Definicão das rotas da aplicação"""

from app.routes.auth import define_auth_routes
from app.routes.transactions import define_transaction_routes
from app.routes.account import define_account_routes

from flask_cors import CORS
from flask import jsonify, request

import jwt

from . import db
from . import create_app

app = create_app()

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

with app.app_context():
    db.create_all()

@app.before_request
def is_authenticated():
    """Verifica se o usuário está autenticado"""

    if request.path in ['/signin', '/signup']:
        pass
    else:
        token = request.headers.get('token', None)
        try:
            jwt.decode(token.encode(), 'secret_token')
        except ValueError:
            return jsonify({"message": "Não Autorizado. Faça Login"}), 403

define_auth_routes(app, db)
define_transaction_routes(app, db)
define_account_routes(app, db)

app.run()
