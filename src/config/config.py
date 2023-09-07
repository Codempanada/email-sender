from dotenv import load_dotenv
import os


load_dotenv()


class Config(object):
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = int(os.environ['MAIL_PORT'])
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_USE_TLS = bool(os.environ['MAIL_USE_TLS'])
    MAIL_USE_SSL = bool(os.environ['MAIL_USE_SSL'])


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
