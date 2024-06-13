from models.bus import Bus
from models.bus_owner import BusOwner
from models.route import Route

def add_owner_cli():
    first_name = input("Enter owner's first name: ")
    last_name = input("Enter owner's last name: ")
    phone_no = input("Enter phone number: ")
    BusOwner.add(first_name, last_name, phone_no)
    print("Owner added successfully!")

def view_owners_cli():
    owners = BusOwner.get_all()
    print("Bus Owners:")
    for owner in owners:
        print(f"ID: {owner.owner_id}, Name: {owner.first_name} {owner.last_name}, Phone: {owner.phone_no}")

def update_owner_cli():
    owner_id = int(input("Enter owner ID to update: "))
    owner = BusOwner.get_by_id(owner_id)
    if owner:
        first_name = input("Enter new first name: ")
        last_name = input("Enter new last name: ")
        phone_no = input("Enter new phone number: ")
        owner.update(first_name, last_name, phone_no)
        print("Owner updated successfully!")
    else:
        print("Owner not found.")

def delete_owner_cli():
    owner_id = int(input("Enter owner ID to delete: "))
    owner = BusOwner.get_by_id(owner_id)
    if owner:
        owner.delete()
        print("Owner deleted successfully!")
    else:
        print("Owner not found.")

def add_bus_cli():
    registration_no = input("Enter registration number: ")
    owner_id = int(input("Enter owner ID: "))
    route_id = int(input("Enter route ID: "))
    Bus.add(registration_no, owner_id, route_id)
    print("Bus added successfully!")

def view_buses_cli():
    buses = Bus.get_all()
    print("Buses:")
    for bus in buses:
        owner = bus.get_owner_info()
        print(f"ID: {bus.bus_id}, Registration: {bus.registration_no}, Owner: {owner.first_name} {owner.last_name}, Route: {bus.route_id}")

def update_bus_cli():
    bus_id = int(input("Enter bus ID to update: "))
    bus = Bus.get_by_id(bus_id)
    if bus:
        registration_no = input("Enter new registration number: ")
        owner_id = int(input("Enter new owner ID: "))
        route_id = int(input("Enter new route ID: "))
        bus.update(registration_no, owner_id, route_id)
        print("Bus updated successfully!")
    else:
        print("Bus not found.")

def delete_bus_cli():
    bus_id = int(input("Enter bus ID to delete: "))
    bus = Bus.get_by_id(bus_id)
    if bus:
        bus.delete()
        print("Bus deleted successfully!")
    else:
        print("Bus not found.")

def add_route_cli():
    route_name = input("Enter route name: ")
    Route.add(route_name)
    print("Route added successfully!")

def view_routes_cli():
    routes = Route.get_all()
    print("Routes:")
    for route in routes:
        print(f"ID: {route.route_id}, Name: {route.route_name}")

def update_route_cli():
    route_id = int(input("Enter route ID to update: "))
    route = Route.get_by_id(route_id)
    if route:
        route_name = input("Enter new route name: ")
        route.update(route_name)
        print("Route updated successfully!")
    else:
        print("Route not found.")

def delete_route_cli():
    route_id = int(input("Enter route ID to delete: "))
    route = Route.get_by_id(route_id)
    if route:
        route.delete()
        print("Route deleted successfully!")
    else:
        print("Route not found.")

def main():
    while True:
        print("Welcome to Bus Sacco Management System")
        print("1. Add Bus Owner")
        print("2. View Bus Owners")
        print("3. Update Bus Owner")
        print("4. Delete Bus Owner")
        print("5. Add Bus")
        print("6. View Buses")
        print("7. Update Bus")
        print("8. Delete Bus")
        print("9. Add Route")
        print("10. View Routes")
        print("11. Update Route")
        print("12. Delete Route")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_owner_cli()
        elif choice == '2':
            view_owners_cli()
        elif choice == '3':
            update_owner_cli()
        elif choice == '4':
            delete_owner_cli()
        elif choice == '5':
            add_bus_cli()
        elif choice == '6':
            view_buses_cli()
        elif choice == '7':
            update_bus_cli()
        elif choice == '8':
            delete_bus_cli()
        elif choice == '9':
            add_route_cli()
        elif choice == '10':
            view_routes_cli()
        elif choice == '11':
            update_route_cli()
        elif choice == '12':
            delete_route_cli()
        elif choice == '13':
            print("Thank you for using Bus Sacco Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
