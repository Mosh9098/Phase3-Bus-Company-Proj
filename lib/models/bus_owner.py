from db.connection import get_db_connection

class BusOwner:
    def __init__(self, owner_id, first_name, last_name, phone_no):
        # Initialize the BusOwner instance with the provided attributes
        self._owner_id = owner_id
        self._first_name = first_name
        self._last_name = last_name
        self._phone_no = phone_no

    def __repr__(self):
        # Define the string representation of the BusOwner instance
        return f'<BusOwner {self.first_name} {self.last_name}>'

    # Define the owner_id property with a getter method
    @property
    def owner_id(self):
        return self._owner_id

    # Define the first_name property with a getter method
    @property
    def first_name(self):
        return self._first_name

    # Define the setter method for the first_name property
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("First name must be a non-empty string")
        self._first_name = value

    # Define the last_name property with a getter method
    @property
    def last_name(self):
        return self._last_name

    # Define the setter method for the last_name property
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Last name must be a non-empty string")
        self._last_name = value

    # Define the phone_no property with a getter method
    @property
    def phone_no(self):
        return self._phone_no

    # Define the setter method for the phone_no property
    @phone_no.setter
    def phone_no(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Phone number must be a non-empty string")
        self._phone_no = value

    # Define a class method to add a new BusOwner to the database
    @classmethod
    def add(cls, first_name, last_name, phone_no):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO BusOwner (OwnerFirstName, OwnerLastName, PhoneNo) VALUES (?, ?, ?)', (first_name, last_name, phone_no))
        conn.commit()
        conn.close()

    # Define a class method to retrieve a BusOwner by their ID
    @classmethod
    def get_by_id(cls, owner_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM BusOwner WHERE OwnerID = ?', (owner_id,))
        owner_data = cursor.fetchone()
        conn.close()
        if owner_data:
            return cls(owner_data['OwnerID'], owner_data['OwnerFirstName'], owner_data['OwnerLastName'], owner_data['PhoneNo'])
        return None

    # Define a class method to retrieve all BusOwner instances from the database
    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM BusOwner')
        owners_data = cursor.fetchall()
        conn.close()
        return [cls(owner['OwnerID'], owner['OwnerFirstName'], owner['OwnerLastName'], owner['PhoneNo']) for owner in owners_data]

    # Define an instance method to update the current BusOwner's information in the database
    def update(self, first_name, last_name, phone_no):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE BusOwner SET OwnerFirstName = ?, OwnerLastName = ?, PhoneNo = ? WHERE OwnerID = ?', (first_name, last_name, phone_no, self.owner_id))
        conn.commit()
        conn.close()

    # Define an instance method to delete the current BusOwner from the database
    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM BusOwner WHERE OwnerID = ?', (self.owner_id,))
        conn.commit()
        conn.close()
