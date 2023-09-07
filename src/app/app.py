# Flask modules
from flask import Flask
# flask mail from module
from .mail import mail
# Config from module
from config.config import config


def create_app(config_name) -> Flask:
    app = Flask(__name__)
    
    # Config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)  
    app.config.from_pyfile('../config/config.py')
    
    # Init Mail app
    mail.init_app(app)
    print(config_name)
    return app.run()