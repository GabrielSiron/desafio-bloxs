import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL")
    SECRET_KEY = 'wq91x2jcb44jdjdaxsx'

config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}

