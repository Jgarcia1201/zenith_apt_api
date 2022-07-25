from flask import current_app
from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv

load_dotenv()


class DBConnection:
    connection = None
    cursor = None

    def __init__(self):
        mysql = MySQL()
        mysql.init_app(current_app)
        self.connection = mysql.connect
        self.cursor = self.connection.cursor()

    def get_db_cursor(self):
        return self.cursor

    def is_connected(self):
        if self.connection is not None:
            return True
        else:
            return False
