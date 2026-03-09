
from database import get_connection

cnx = get_connection()

if cnx:
    print("Connected successfully!")
    cnx.close()
else:
    print("Connection failed.")
