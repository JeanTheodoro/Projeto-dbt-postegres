import os
import psycopg2

from dotenv import load_dotenv
# Load Envirioment
load_dotenv()

class PostgresSingleton:
    _instance = None
    _connection = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PostgresSingleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._connection is None:
            self._connection = psycopg2.connect(
                host=os.getenv("POSTGRES_HOST"),
                database=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                port="5432"
                )
    
    def get_connection(self):
        return self._connection
