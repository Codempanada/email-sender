# Flask modules
from flask import Flask
# flask mail from module
from .extensions import mail
# handler
from .handler import register_error_handlers
# Config from module
from config.config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    mail.init_app(app)
    
    register_error_handlers(app)
    """ Blueprints """
    from .route import email
    app.register_blueprint(email)    
    
    return app