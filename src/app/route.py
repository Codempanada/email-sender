# Flask modules
from flask import request
from flask import jsonify
from flask import Blueprint
from flask_mail import Message
# Local modules
from .extensions import mail
from config.config import email_detail


email = Blueprint('email', __name__, url_prefix='/mail')


@email.route('/send', methods=["POST"])
def send_email():
    try:
        if request.headers.get('Auth-Code') != email_detail['Auth-Code']:     
            return jsonify(
                response="You are not Authorized",
                status=401
            )
        
        
        msg = Message(
            subject=request.json['subject'],
            body=request.json['body'],
            recipients=email_detail['Recipients']
        )

        mail.send(msg)
        
        return jsonify(
            response="The mail has been sent correctly",
            status=200,
        )

    except Exception as ex:
        print(ex)
        return jsonify(
            response="Something Gone Wrong, The mail couldn't be sent",
            status=500,
        )
