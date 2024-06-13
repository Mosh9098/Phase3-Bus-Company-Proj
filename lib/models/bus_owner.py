from db.connection import get_db_connection

class BusOwner:
    def __init__(self, owner_id, first_name, last_name, phone_no):
        self._owner_id = owner_id
        self._first_name = first_name
        self._last_name = last_name
        self._phone_no = phone_no

    def __repr__(self):
        return f'<BusOwner {self.first_name} {self.last_name}>'

    @property
    def owner_id(self):
        return self._owner_id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("First name must be a non-empty string")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Last name must be a non-empty string")
        self._last_name = value

    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Phone number must be a non-empty string")
        self._phone_no = value

    @classmethod
    def add(cls, first_name, last_name, phone_no):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO BusOwner (OwnerFirstName, OwnerLastName, PhoneNo) VALUES (?, ?, ?)', (first_name, last_name, phone_no))
        conn.commit()
        conn.close()

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

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM BusOwner')
        owners_data = cursor.fetchall()
        conn.close()
        return [cls(owner['OwnerID'], owner['OwnerFirstName'], owner['OwnerLastName'], owner['PhoneNo']) for owner in owners_data]

    def update(self, first_name, last_name, phone_no):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE BusOwner SET OwnerFirstName = ?, OwnerLastName = ?, PhoneNo = ? WHERE OwnerID = ?', (first_name, last_name, phone_no, self.owner_id))
        conn.commit()
        conn.close()

    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM BusOwner WHERE OwnerID = ?', (self.owner_id,))
        conn.commit()
        conn.close()
