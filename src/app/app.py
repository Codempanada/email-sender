# Flask modules
from flask import Flask
# flask mail from module
from .extensions import mail, cors
# handler
from .handler import register_error_handlers
# Config from module
from config.config import config
from config.config import ORIGIN


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    mail.init_app(app)
    cors.init_app(app, origins=['localhost:4200', ORIGIN], methods=['POST'],)

    register_error_handlers(app)
    
    """ Blueprints """
    from .route import email
    app.register_blueprint(email)

    return app