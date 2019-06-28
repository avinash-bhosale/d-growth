import os
from datetime import timedelta


class Config(object):
    CORS_HEADERS = 'Content-Type'
    SECRET_KEY = 'ASSdsWFG5GE65R8EG4H4TRRS6FG46S4G8RG6S'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kn@ambrosial@localhost/dgrowth_db'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_EMAIL = 'contact@agileinfo.com'


class ProductionConfig(Config):
    # DEBUG = False
    ADMIN_EMAIL = 'contact@agileinfo.com'


class DebugConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


config_dict = {
    'Production': ProductionConfig,
    'Development': DevelopmentConfig,
    'Debug': DebugConfig
}
