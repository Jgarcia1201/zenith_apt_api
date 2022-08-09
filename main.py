from flask import Flask
from controller.complex_controller import complex_controller
from controller.contact_controller import contact_controller
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config['MYSQL_DATABASE_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('DB_PASS')
app.config["MYSQL_DATABASE_DB"] = os.environ.get('DB_NAME')
app.config["MYSQL_DATABASE_HOST"] = os.environ.get('Surface')

app.register_blueprint(complex_controller, url_prefix="/getApts")
app.register_blueprint(contact_controller, url_prefix="/email")

if __name__ == '__main__':
    app.run()
