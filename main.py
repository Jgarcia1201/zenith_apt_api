from flask import Flask
from controller.complex_controller import complex_controller

app = Flask(__name__)

app.register_blueprint(complex_controller, url_prefix="/getApts")

app.run()
