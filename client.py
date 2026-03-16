# client.py
from database import execute
 
class Client:
    def __init__(self, name: str, company: str, email: str, phone: str):
        self.name = name.strip()
        self.company = (company or "").strip()
        self.email = (email or "").strip()
        self.phone = (phone or "").strip()
 
    def is_valid(self):
        if not self.name:
            print("Client name is required.")
            return False
        return True  # BRD only requires basic validation
                     # (required fields not blank), keep it simple
    def save(self):
        if not self.is_valid():
            return None
        q = """INSERT INTO clients (name, company, email, phone)
               VALUES (%s, %s, %s, %s)"""
        return execute(q, (self.name, self.company, self.email, self.phone))
 
    @staticmethod
    def list_all():
        q = """SELECT client_id, name, company, email, phone
               FROM clients ORDER BY client_id"""
        return execute(q, fetch=True)
 
    @staticmethod
    def exists(client_id: int):
        q = "SELECT 1 FROM clients WHERE client_id = %s"
        return bool(execute(q, (client_id,), fetch=True))