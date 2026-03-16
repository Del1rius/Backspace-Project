# subscription.py
from database import execute
from client import Client
 
VAT_RATE = 0.15  # BRD rule
 
class Subscription:
    @staticmethod
    def _get_service(service_id: int):
        q = "SELECT service_id, name, price FROM services WHERE service_id = %s"
        rows = execute(q, (service_id,), fetch=True)
        return rows[0] if rows else None
 
    @staticmethod
    def activate(client_id: int, service_id: int):
        # Validate existence (BRD: client must exist, service must exist)
        if not Client.exists(client_id):
            print("Client does not exist.")
            return None
 
        service = Subscription._get_service(service_id)
        if not service:
            print("Service does not exist.")
            return None
 
        subtotal = float(service["price"])
        vat = round(subtotal * VAT_RATE, 2)
        total = round(subtotal + vat, 2)
 
        q = """INSERT INTO subscriptions (client_id, service_id, subtotal, vat, total)
               VALUES (%s, %s, %s, %s, %s)"""
        sub_id = execute(q, (client_id, service_id, subtotal, vat, total))
        if sub_id:
            print("Service Activated Successfully")
            print(f"Client ID: {client_id}")
            print(f"Service: {service['name']}")
            print(f"Price: R{subtotal:.2f}")
            print(f"VAT (15%): R{vat:.2f}")
            print(f"Total: R{total:.2f}")
        return sub_id