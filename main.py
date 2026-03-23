from service import Service
from client import Client
from subscription import Subscription

def add_service():
    name = input("Service Name: ")
    desc = input("Description: ")
    price = input("Price: ")

    try:
        price = float(price)
    except ValueError:
        print("Price must be numeric!")
        return
    
    s = Service(name, desc, price)
    sid = s.save()
    print(f"Service added with ID {sid}") if sid else None

def view_service():
    rows = Service.list_all()
    if not rows:
        print("No services found.")
        return
    for r in rows:
        print(f"{r['service_id']}. {r['name']} - {r['description']} - R{r['price']:.2f}")

def register_client():
    name = input("Client Name: ")
    company = input("Company: ")
    email = input("Email: ")
    phone = input("Phone: ")

    c = Client(name, company, email, phone)
    cid = c.save()
    print(f"Client registered with ID {cid}") if cid else None
    
def view_client():
    rows = Client.list_all()

    if not rows:
        print("No clients found.")
        return
    for r in rows:
        print(f"{r['client_id']}. {r['name']} - {r['company']} - {r['email']} - {r['phone']}")

def activate_service():
    try:
        client_id = int(input("Client ID: "))
        service_id = int(input("Service ID: "))
    except ValueError:
        print("ID's must be integers.")
        return
    Subscription.activate(client_id, service_id)

def main_menu():
    while True:
        print("\BACKSPACE TECHNOLOGIES SERVICE SYSTEM")
        print("1. Add Service")
        print("2. View Services")
        print("3. Register Client")
        print("4. View Client")
        print("5. Activate Service")
        print("6. Exit")
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            add_service()
        elif choice == "2":
            view_service()
        elif choice == "3":
            register_client()
        elif choice == "4":
            view_client()
        elif choice == "5":
            activate_service()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid Option choose between 1 and 6.")


if __name__ == "__main__":
    main_menu()

