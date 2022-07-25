from db import DBConnection

'''
Eventually will be able to instantiate a class with a mysql connection and make queries to the database.
These will be returned to the repository layer where they will be processed and passed into the controller layer
and finally passed on to the client through the controller layer.
'''


class ComplexService:
    cursor = None

    def __init__(self):
        conn = DBConnection()
        db_cursor = conn.get_db_cursor()
