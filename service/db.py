from flask import current_app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
load_dotenv()

'''
Creates an instance of DB Connection to make a query.
Should only be accessed by the Service layer.
'''


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
