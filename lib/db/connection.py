import sqlite3

# Specify the path to the SQLite database file
DATABASE_NAME = './db/BusCompany.db'

# Function to establish a connection to the database
def get_db_connection():
    # Connect to the SQLite database using the specified database file
    conn = sqlite3.connect(DATABASE_NAME)
    
    # Set the row factory to sqlite3.Row to access columns by name
    conn.row_factory = sqlite3.Row
    
    # Return the connection object
    return conn
