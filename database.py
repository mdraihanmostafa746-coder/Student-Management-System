import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connect_database():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")   
        )

        return connection

    except Exception as error:
        print("Database Connection Failed!")
        print(error)
        return None
    
    