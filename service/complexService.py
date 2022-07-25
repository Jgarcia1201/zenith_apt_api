from db import DBConnection


class ComplexService:
    cursor = None

    def __init__(self):
        conn = DBConnection()
        self.cursor = conn.get_db_cursor()
