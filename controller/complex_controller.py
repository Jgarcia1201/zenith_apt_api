from flask import Blueprint
from service.complexService import ComplexService

complex_controller = Blueprint('complex_controller', __name__)


@complex_controller.route('/')
def get_apts():
    db_cursor = ComplexService().cursor
    return None

