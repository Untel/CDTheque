import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST =  os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
class Database:
    
    def __init__(self):
        self.conn = mysql.connector.connect(host=DATABASE_HOST,
                                            user=DATABASE_USER,
                                            password=DATABASE_PASSWORD,
                                            database=DATABASE_NAME)

    def close(self):
        self.conn.close()

    def query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor
