from flask import Blueprint
from repository.complexRepo import get_complexes
from service.emailService import send_to_agent
import json

complex_controller = Blueprint('complex_controller', __name__)

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

test_client = {
    'name': 'James',
    'email': 'james@james.com',
    'hoods': ['Heights', 'WestU', 'Midtown'],
    'lux_score': 7,
    'liv_score': 5,
    'rent_min': 0,
    'rent_max': 1600,
    "pets": True,
    "desiredBr": 1
}


@complex_controller.route('/')
def get_apts():
    send_to_agent()
    get_complexes(test_client)
    return 0
