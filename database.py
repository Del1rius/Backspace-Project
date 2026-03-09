
# database.py
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()  # reads .env in project root

def get_connection():
    try:
        cnx = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
        return cnx
    except Error as e:
        print(f"[DB] Connection error: {e}")
        return None

def execute(query, params=None, fetch=False):
    """
    Run a SQL statement.
    - fetch=False: commit & return lastrowid
    - fetch=True : return list of rows (dicts)
    """
    cnx = get_connection()
    if not cnx:
        return None
    try:
        with cnx.cursor(dictionary=True) as cur:
            cur.execute(query, params or ())
            if fetch:
                return cur.fetchall()
            cnx.commit()
            return cur.lastrowid
    except Error as e:
        print(f"[DB] Query error: {e}")
        return None
    finally:
        cnx.close()
