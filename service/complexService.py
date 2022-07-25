from service.db import DBConnection

'''
Accesses DB Connection and makes a query.
Should be accessed by the repository layer ONLY. 
Should never contact controller layer directly.
'''


class ComplexService:
    cursor = None
    conn = None

    def __init__(self):
        self.conn = DBConnection().connection
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.conn.close()
        return data
