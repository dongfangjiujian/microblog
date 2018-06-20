import os
basedir = os.path.abspath(os.path.dirname(__file__))
print("basedir : "+basedir)\

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this key is very hard to guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
    BABEL_DEFAULT_LOCALE='zh'
    DEBUG=True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test.db')
    DEBUG = True

config = {
    'development':DevelopmentConfig,
    'test':TestConfig,
    'default':DevelopmentConfig
}