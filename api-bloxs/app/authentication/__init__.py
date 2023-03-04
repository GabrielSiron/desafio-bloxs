from flask import request

class Authentication:
    validSessions = []

    @classmethod
    def create_session(cls, token, account_id):
        from datetime import date, datetime
        from dateutil.relativedelta import relativedelta

        cls.validSessions.append(
            {
                'token': token,
                'account_id': account_id,
                'expire_at': datetime.now() + relativedelta(months=3)
            }
        )

    @classmethod
    def is_authenticated(cls, token):
        from datetime import datetime
        for index, session in enumerate(cls.validSessions):
            if session['token'] == token:
                if session['expire_at'] > datetime.now():
                    break
                else:
                    validSessions.pop(index)
        else:
            return False
        
        return True

    @staticmethod
    def generate_token(req):
        import jwt
        import datetime

        token = jwt.encode({'email': req.json['email'], 'exp': datetime.datetime.now()}, 'aksdkan2n12j')
        return token

    @classmethod
    def find_id_by_token(cls, token):
        for session in cls.validSessions:
            if session['token'] == token:
                return session['account_id']