from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gabriel:143867@localhost/db?host=localhost?port=8080'
db = SQLAlchemy(app)

class BaseClass:
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, onupdate=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=db.func.utc_timestamp())