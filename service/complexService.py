from flask import current_app

'''
Eventually will be able to instantiate a class with a mysql connection and make queries to the database.
These will be returned to the repository layer where they will be processed and passed into the controller layer
and finally passed on to the client through the controller layer.
'''


class ComplexService:

    def __init__(self, connection):
        self.connection = connection.connect
