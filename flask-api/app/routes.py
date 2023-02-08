import os

from flask import jsonify

from . import create_app
from . import db

from .models.account import Account
from .models.account_type import AccountType
from .models.transaction import Transaction

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

app.app_context().push()

db.create_all()

@app.route('/')
def index():
    return jsonify({"message": "Olá, Mundo!"})
    
app.run()