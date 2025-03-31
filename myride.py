import MySQLdb
from MySQLdb import Error
from datetime import datetime

# Database connection details
my_conn = {
    "host": "e3bc9e1a0b71.601a9382.alu-cod.online",
    "user": "Jonathan2005",
    "port": 38775,
    "password": "Munyeshuri@2005",
    "database": "myride"
}

# Connect to the database
def connect_db():
    try:
        connection = MySQLdb.connect(
            host=my_conn["host"],
            user=my_conn["user"],
            passwd=my_conn["password"],
            db=my_conn["database"],
            port=my_conn["port"]
        )
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Driver registration
def add_driver():
    connection = connect_db()
    if connection:
        print("Enter your credentials to register")
        driver_name = input("Enter your name: ")
        driver_phone = input("Enter your phone number: ")
        driver_password = input("Enter your password: ")
        available_seats = int(input("Enter the number of available seats in your car: "))
        current_location = input("Enter your current location: ")
        destination = input("Enter your destination: ")
        
        try:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO driver (DriverName, DriverPhoneNumber, DriverPassword, AvailableSeats, CurrentLocation, Destination)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (driver_name, driver_phone, driver_password, available_seats, current_location, destination))
            connection.commit()
            print(f"Driver {driver_name} registered successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Passenger registration
def add_passenger():
    connection = connect_db()
    if connection:
        print("Enter your details to register")
        passenger_name = input("Enter your name: ")
        passenger_phone = input("Enter your phone number: ")
        pickup_location = input("Enter your pickup location: ")
        destination = input("Enter your destination: ")
        
        try:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO Passenger (PassengerName, PassengerPhoneNumber, PickupLocation, Destination)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (passenger_name, passenger_phone, pickup_location, destination))
            connection.commit()
            print(f"Passenger {passenger_name} registered successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Match drivers and passengers
def match_driver_to_passenger():
    connection = connect_db()
    if connection:
        passenger_destination = input("Enter your destination: ")
        try:
            cursor = connection.cursor()
            query = """
            SELECT * FROM Driver WHERE Destination = %s AND AvailableSeats > 0
            """
            cursor.execute(query, (passenger_destination,))
            drivers = cursor.fetchall()
            if drivers:
                print("Available drivers:")
                for driver in drivers:
                    print(f"Driver Name: {driver[1]}, Phone: {driver[2]}, Seats Available: {driver[4]}, Location: {driver[5]}")
            else:
                print("No drivers available for your destination.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Add trip
def add_trip(driver_id, passenger_id, price):
    connection = connect_db()
    if connection:
        trip_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO Trips (DriverId, PassengerId, Price, TripDate)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (driver_id, passenger_id, price, trip_date))
            connection.commit()
            print("Trip added successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
# Admin dashboard
def admin_dashboard():
    connection = connect_db()
    if connection:
        print("Admin Dashboard")
        while True:
            print("\nMenu:")
            print("1. View Drivers")
            print("2. View Passengers")
            print("3. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                view_drivers(connection)
            elif choice == '2':
                view_passengers(connection)
            elif choice == '3':
                print("Exiting Admin Dashboard...")
                break
            else:
                print("Invalid choice. Please try again.")
        connection.close()

def view_drivers(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM Driver"
        cursor.execute(query)
        drivers = cursor.fetchall()
        if drivers:
            print("Driver Details:")
            for driver in drivers:
                print(f"ID: {driver[0]}, Name: {driver[1]}, Phone: {driver[2]}, Seats Available: {driver[4]}, Location: {driver[5]}, Destination: {driver[6]}")
        else:
            print("No drivers available.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def view_passengers(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM Passenger"
        cursor.execute(query)
        passengers = cursor.fetchall()
        if passengers:
            print("Passenger Details:")
            for passenger in passengers:
                print(f"ID: {passenger[0]}, Name: {passenger[1]}, Phone: {passenger[2]}, Pickup Location: {passenger[3]}, Destination: {passenger[4]}")
        else:
            print("No passengers registered.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

# Admin login
def admin_login():
    connection = connect_db()
    if connection:
        admin_name = input("Enter your admin name: ")
        admin_password = input("Enter your admin password: ")
        try:
            cursor = connection.cursor()
            query = """
            SELECT * FROM Admin WHERE AdminName = %s AND AdminPassword = %s
            """
            cursor.execute(query, (admin_name, admin_password))
            admin = cursor.fetchone()
            if admin:
                print(f"Welcome, {admin_name}!")
                admin_dashboard()
            else:
                print("Invalid credentials. Please try again.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()


# Main menu
def main_menu():
    print("Welcome to My Ride!")
    while True:
        print("\nMenu:")
        print("1. Register as Driver")
        print("2. Register as Passenger")
        print("3. Find a Ride")
        print("4. Admin Login")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_driver()
        elif choice == '2':
            add_passenger()
        elif choice == '3':
            match_driver_to_passenger()
        elif choice == '4':
            admin_login()
        elif choice == '5':
            print("Thank you for using My Ride. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main_menu()
# import MySQLdb
# from MySQLdb import Error
# from datetime import datetime

# # Database connection details
# my_conn = {
#     "host": "e3bc9e1a0b71.601a9382.alu-cod.online",
#     "user": "Jonathan2005",
#     "port": 38775,
#     "password": "Munyeshuri@2005",
#     "database": "myride"
# }

# # Connect to the database
# def connect_db():
#     try:
#         connection = MySQLdb.connect(
#             host=my_conn["host"],
#             user=my_conn["user"],
#             passwd=my_conn["password"],
#             db=my_conn["database"],
#             port=my_conn["port"]
#         )
#         return connection
#     except Error as e:
#         print(f"Error connecting to database: {e}")
#         return None

# # Driver registration
# def add_driver():
#     connection = connect_db()
#     if connection:
#         print("Enter your credentials to register")
#         driver_name = input("Enter your name: ")
#         driver_phone = input("Enter your phone number: ")
#         driver_password = input("Enter your password: ")
#         available_seats = int(input("Enter the number of available seats in your car: "))
#         current_location = input("Enter your current location: ")
#         destination = input("Enter your destination: ")
        
#         try:
#             cursor = connection.cursor()
#             insert_query = """
#             INSERT INTO Driver (DriverName, DriverPhoneNumber, DriverPassword, AvailableSeats, CurrentLocation, Destination)
#             VALUES (%s, %s, %s, %s, %s, %s)
#             """
#             cursor.execute(insert_query, (driver_name, driver_phone, driver_password, available_seats, current_location, destination))
#             connection.commit()
#             print(f"Driver {driver_name} registered successfully!")
#         except Error as e:
#             print(f"Error: {e}")
#         finally:
#             cursor.close()
#             connection.close()

# # Passenger registration
# def add_passenger():
#     connection = connect_db()
#     if connection:
#         print("Enter your details to register")
#         passenger_name = input("Enter your name: ")
#         passenger_phone = input("Enter your phone number: ")
#         pickup_location = input("Enter your pickup location: ")
#         destination = input("Enter your destination: ")
        
#         try:
#             cursor = connection.cursor()
#             insert_query = """
#             INSERT INTO Passenger (PassengerName, PassengerPhoneNumber, PickupLocation, Destination)
#             VALUES (%s, %s, %s, %s)
#             """
#             cursor.execute(insert_query, (passenger_name, passenger_phone, pickup_location, destination))
#             connection.commit()
#             print(f"Passenger {passenger_name} registered successfully!")
#         except Error as e:
#             print(f"Error: {e}")
#         finally:
#             cursor.close()
#             connection.close()

# # Find Ride Feature
# def find_ride():
#     print("\nFind Ride")
#     while True:
#         print("\nAre you continuing as:")
#         print("1. Passenger")
#         print("2. Driver")
#         print("3. Exit to Main Menu")
#         choice = input("Enter your choice: ")
        
#         if choice == '1':  # Passenger
#             passenger_actions()
#         elif choice == '2':  # Driver
#             driver_actions()
#         elif choice == '3':  # Exit
#             print("Returning to the main menu...")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# # Passenger Options
# def passenger_actions():
#     connection = connect_db()
#     if connection:
#         print("\nPassenger Actions")
#         while True:
#             print("\nOptions:")
#             print("1. Register as Passenger")
#             print("2. View Assigned Driver")
#             print("3. Return to Previous Menu")
#             choice = input("Enter your choice: ")
            
#             if choice == '1':  # Register
#                 add_passenger()
#             elif choice == '2':  # View Assigned Driver
#                 passenger_id = input("Enter your Passenger ID: ")
#                 view_assigned_driver(passenger_id, connection)
#             elif choice == '3':  # Exit
#                 print("Returning to Find Ride menu...")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")
#         connection.close()

# def view_assigned_driver(passenger_id, connection):
#     try:
#         cursor = connection.cursor()
#         query = """
#         SELECT d.DriverName, d.DriverPhoneNumber, d.CurrentLocation, d.Destination 
#         FROM Trips t
#         JOIN Driver d ON t.DriverID = d.DriverID
#         WHERE t.PassengerID = %s
#         """
#         cursor.execute(query, (passenger_id,))
#         driver = cursor.fetchone()
#         if driver:
#             print(f"\nAssigned Driver Details:")
#             print(f"Name: {driver[0]}")
#             print(f"Phone: {driver[1]}")
#             print(f"Location: {driver[2]}")
#             print(f"Destination: {driver[3]}")
#         else:
#             print("No driver is currently assigned to you.")
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         cursor.close()

# # Driver Options
# def driver_actions():
#     connection = connect_db()
#     if connection:
#         print("\nDriver Actions")
#         while True:
#             print("\nOptions:")
#             print("1. Log in as Driver")
#             print("2. Return to Previous Menu")
#             choice = input("Enter your choice: ")
            
#             if choice == '1':  # Log in
#                 driverName = input("Enter your Driver Name: ")
#                 driver_password = input("Enter your Driver Password: ")
#                 if validate_driver(driverName, driver_password, connection):
#                     view_assigned_passengers(driverName, connection)
#                 else:
#                     print("Invalid credentials. Please try again.")
#             elif choice == '2':  # Exit
#                 print("Returning to Find Ride menu...")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")
#         connection.close()

# def validate_driver(driverName, driver_password, connection):
#     try:
#         cursor = connection.cursor()
#         query = """
#         SELECT * FROM Driver WHERE DriverName = %s AND DriverPassword = %s
#         """
#         cursor.execute(query, (driverName, driver_password))
#         driver = cursor.fetchone()
#         return bool(driver)
#     except Error as e:
#         print(f"Error: {e}")
#         return False
#     finally:
#         cursor.close()

# def view_assigned_passengers(driver_id, connection):
#     try:
#         cursor = connection.cursor()
#         query = """
#         SELECT p.PassengerName, p.PassengerPhoneNumber, p.PickupLocation, p.Destination 
#         FROM Trips t
#         JOIN Passenger p ON t.PassengerID = p.PassengerID
#         WHERE t.DriverID = %s
#         """
#         cursor.execute(query, (driver_id,))
#         passengers = cursor.fetchall()
#         if passengers:
#             print("\nAssigned Passengers:")
#             for passenger in passengers:
#                 print(f"Name: {passenger[0]}, Phone: {passenger[1]}, Pickup: {passenger[2]}, Destination: {passenger[3]}")
#         else:
#             print("No passengers are currently assigned to you.")
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         cursor.close()

# # Admin Dashboard
# def admin_dashboard():
#     connection = connect_db()
#     if connection:
#         print("Admin Dashboard")
#         while True:
#             print("\nMenu:")
#             print("1. View Drivers")
#             print("2. View Passengers")
#             print("3. Exit")
#             choice = input("Enter your choice: ")
            
#             if choice == '1':
#                 view_drivers(connection)
#             elif choice == '2':
#                 view_passengers(connection)
#             elif choice == '3':
#                 print("Exiting Admin Dashboard...")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")
#         connection.close()

# def view_drivers(connection):
#     try:
#         cursor = connection.cursor()
#         query = "SELECT * FROM Driver"
#         cursor.execute(query)
#         drivers = cursor.fetchall()
#         if drivers:
#             print("Driver Details:")
#             for driver in drivers:
#                 print(f"ID: {driver[0]}, Name: {driver[1]}, Phone: {driver[2]}, Seats Available: {driver[4]}, Location: {driver[5]}, Destination: {driver[6]}")
#         else:
#             print("No drivers available.")
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         cursor.close()

# def view_passengers(connection):
#     try:
#         cursor = connection.cursor()
#         query = "SELECT * FROM Passenger"
#         cursor.execute(query)
#         passengers = cursor.fetchall()
#         if passengers:
#             print("Passenger Details:")
#             for passenger in passengers:
#                 print(f"ID: {passenger[0]}, Name: {passenger[1]}, Phone: {passenger[2]}, Pickup Location: {passenger[3]}, Destination: {passenger[4]}")
#         else:
#             print("No passengers registered.")
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         cursor.close()

# # Admin login
# def admin_login():
#     connection = connect_db()
#     if connection:
#         admin_name = input("Enter your admin name: ")
#         admin_password = input("Enter your admin password: ")
#         try:
#             cursor = connection.cursor()
#             query = """
#             SELECT * FROM Admin WHERE AdminName = %s AND AdminPassword = %s
#             """
#             cursor.execute(query, (admin_name, admin_password))
#             admin = cursor.fetchone()
#             if admin:
#                 print(f"Welcome, {admin_name}!")
#                 admin_dashboard()
#             else:
#                 print("Invalid credentials. Please try again.")
#         except Error as e:
#             print(f"Error: {e}")
#         finally:
#             cursor.close()
#             connection.close()

# def main_menu():
#     print("Welcome to MY RIDE!")
#     while True:
#         print("\nMenu:")
#         print("1. Register as Driver")
#         print("2. Register as Passenger")
#         print("3. Find a Ride")
#         print("4. Admin Login")
#         print("5. Exit")
#         choice = input("Enter your choice: ")
        
#         if choice == '1':  # Driver Registration
#             add_driver()
#         elif choice == '2':  # Passenger Registration
#             add_passenger()
#         elif choice == '3':  # Find Ride Logic
#             find_ride()
#         elif choice == '4':  # Admin Login
#             admin_login()
#         elif choice == '5':  # Exit Program
#             print("Thank you for using MY RIDE. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")
# main_menu()