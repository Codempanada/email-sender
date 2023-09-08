from dotenv import load_dotenv
import os


load_dotenv()


class Config(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = int(os.environ['MAIL_PORT'])
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_DEFAULT_SENDER = os.environ['MAIL_USERNAME']
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', True)


class TestingConfig(Config):
    TESTING = True


email_detail = {
    "recipients": [
        os.environ['MAIL_USERNAME'],
        os.environ['MAIL_BACK_UP']
    ],
    "secret_code": os.environ['SECRET_CODE']
}

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
