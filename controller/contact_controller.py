from flask import Blueprint, request
from service.emailService import send_contact_email
from flask_cors import cross_origin


contact_controller = Blueprint("contact_controller", __name__)


@contact_controller.route('/', methods=['POST'])
@cross_origin(origins='http://localhost:3000')
def handle_contact_sub():
    email = request.get_json(force=True)
    if len(email["sender"]) > 0 and len(email["message"]) > 0:
        send_contact_email(email)
        return 'message sent'
    return '0'
