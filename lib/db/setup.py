# Import the get_db_connection function from the connection module
from connection import get_db_connection

# Function to create the necessary tables in the database
def create_tables():
    # Establish a database connection
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create the BusOwner table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BusOwner (
            OwnerID INTEGER PRIMARY KEY AUTOINCREMENT,
            OwnerFirstName VARCHAR NOT NULL,
            OwnerLastName VARCHAR NOT NULL,
            PhoneNo VARCHAR NOT NULL
        )
    ''')
    
    # Create the Routes table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Routes (
            RouteID INTEGER PRIMARY KEY AUTOINCREMENT,
            RouteName VARCHAR NOT NULL
        )
    ''')
    
    # Create the Buses table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Buses (
            BusID INTEGER PRIMARY KEY AUTOINCREMENT,
            RegistrationNo VARCHAR NOT NULL,
            OwnerID INTEGER NOT NULL,
            RouteID INTEGER NOT NULL,
            FOREIGN KEY (OwnerID) REFERENCES BusOwner (OwnerID),
            FOREIGN KEY (RouteID) REFERENCES Routes (RouteID)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# If this script is executed directly, create the tables and print a success message
if __name__ == "__main__":
    create_tables()
    print("Database initialized successfully.")
