from flask import current_app
from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os


class DBConnection:

    app = current_app
    connection = None
    cursor = None

    def __init__(self):
        load_dotenv()
        app = current_app
        mysql = MySQL()
        app.config['MYSQL_USER'] = os.environ.get('DB_USER')
        app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASS')
        app.config["MYSQL_DB"] = os.environ.get('DB_NAME')
        app.config["MYSQL_HOST"] = os.environ.get('Surface')
        mysql.init_app(app)
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()

    def get_db_cursor(self):
        return self.cursor

    def is_connected(self):
        if self.connection is not None:
            return True
        else:
            return False
