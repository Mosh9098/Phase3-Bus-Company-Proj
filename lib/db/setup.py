from connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BusOwner (
            OwnerID INTEGER PRIMARY KEY AUTOINCREMENT,
            OwnerFirstName VARCHAR NOT NULL,
            OwnerLastName VARCHAR NOT NULL,
            PhoneNo VARCHAR NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Routes (
            RouteID INTEGER PRIMARY KEY AUTOINCREMENT,
            RouteName VARCHAR NOT NULL
        )
    ''')
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

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database initialized successfully.")
