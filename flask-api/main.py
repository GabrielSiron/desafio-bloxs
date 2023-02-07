import json
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from database import Builder

# from models.base_class import BaseClass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gabriel:143867@0.0.0.0:3306/mysql'
db = SQLAlchemy(app)

Builder.define_tables()
Builder.create_schema()

@app.route('/')
def index():
    return jsonify({"message": "Olá, Mundo!"})

app.run()