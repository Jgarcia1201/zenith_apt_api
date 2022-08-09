from flask import Blueprint, request
from repository.complexRepo import get_complexes
from service.emailService import send_to_agent, send_to_client, send_no_matches
from flask_cors import cross_origin
'''
Will eventually return the top 5 apartments and send them to client through an email.
Also, will send the apt locator the client's information and the apartments and their 
phone number sent to the client through an email.

Currently we have the top 5 apartments returned to this module in an array of objects.
From here we need to send the emails using a template.


Controller 
^^^
Repository
^^^
Service

'''

complex_controller = Blueprint('complex_controller', __name__)


@complex_controller.route('/', methods=['POST'])
@cross_origin(origins='http://localhost:3000')
def get_apts():
    user_client = request.get_json(force=True)
    user_client["matches"] = get_complexes(user_client)
    if len(user_client["matches"]) > 0:
        send_to_agent(user_client)
        send_to_client(user_client)
    else:
        send_no_matches(user_client)
    return '0'
