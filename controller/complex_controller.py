from flask import Blueprint

complex_controller = Blueprint('complex_controller', __name__)


@complex_controller.route('/getApts')
def get_apts():
    return 'test'
