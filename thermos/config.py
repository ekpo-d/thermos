import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'
    DEBUG = False

		
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://xfbwowihpeljve:IkNuK_U856TkT0pYeiFHuCQWIF@ec2-54-243-208-3.compute-1.amazonaws.com:5432/d8rk5mg2lfck7b'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres://xfbwowihpeljve:IkNuK_U856TkT0pYeiFHuCQWIF@ec2-54-243-208-3.compute-1.amazonaws.com:5432/d8rk5mg2lfck7b'
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "localhost"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://xfbwowihpeljve:IkNuK_U856TkT0pYeiFHuCQWIF@ec2-54-243-208-3.compute-1.amazonaws.com:5432/d8rk5mg2lfck7b'


config_by_name = dict(
    dev = DevelopmentConfig,
    test = TestingConfig,
    prod = ProductionConfig
)