# service.py
from database import execute
 
class Service:
    def __init__(self, name: str, description: str, price: float):
        self.name = name.strip()
        self.description = (description or "").strip()
        self.price = price
 
    def is_valid(self):
        if not self.name:
            print("Service name is required.")
        try:
            float(self.price)
        except (TypeError, ValueError):
            print("Service price must be numeric.")
            return False
        return bool(self.name)
 
    def save(self):
        if not self.is_valid():
            return None
        q = """INSERT INTO services (name, description, price)
               VALUES (%s, %s, %s)"""
        return execute(q, (self.name, self.description, self.price))
 
    @staticmethod
    def list_all():
        q = "SELECT service_id, name, description, price FROM services ORDER BY service_id"
        return execute(q, fetch=True)