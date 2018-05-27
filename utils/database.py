import mysql.connector

class Database:
    
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",
                                            user="adrien",
                                            password="MADMAX29",
                                            database="cdtheque")

    def close(self):
        self.conn.close()

    def query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor
