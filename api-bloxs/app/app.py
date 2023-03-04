from . import create_app
from . import db

from app.database import DataBaseConnection

from app.models.account import Account
from app.models.person import Person
from app.models.account_type import AccountType
from app.models.transaction import Transaction

from app.authentication import Authentication

from app.utils import generate_account_object

from app.utils import account_mapping, person_mapping, transaction_mapping, account_type_mapping

from app.routes.auth import define_auth_routes
from app.routes.transactions import define_transaction_routes
from app.routes.account import define_account_routes

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

@app.before_request
def is_authenticated():
    if request.path in ['/signin', '/signup']:
        pass
    else:
        token = request.headers.get('token', None)
        if not token or not Authentication.is_authenticated(token):
            return jsonify({"message": "Não Autorizado. Faça Login"}), 403

define_auth_routes(app, db)
define_transaction_routes(app, db)
define_account_routes(app, db)

app.run()