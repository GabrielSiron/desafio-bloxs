"""Authentication Class"""

import jwt

class Authentication:
    validSessions = []

    @staticmethod
    def generate_token(req, id):
        
        token = jwt.encode({'email': req.json['email'], 'id': id}, 'secret_token')
        return token

    @classmethod
    def find_id_by_token(cls, token):
        
        account = jwt.decode(token, 'secret_token')
        return account['id']