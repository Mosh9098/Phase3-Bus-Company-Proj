from db.connection import get_db_connection
from models.bus_owner import BusOwner

class Bus:
    def __init__(self, bus_id, registration_no, owner_id, route_id):
        self._bus_id = bus_id
        self._registration_no = registration_no
        self._owner_id = owner_id
        self._route_id = route_id

    def __repr__(self):
        return f'<Bus {self.registration_no}>'

    @property
    def bus_id(self):
        return self._bus_id

    @property
    def registration_no(self):
        return self._registration_no

    @registration_no.setter
    def registration_no(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Registration number must be a non-empty string")
        self._registration_no = value

    @property
    def owner_id(self):
        return self._owner_id

    @property
    def route_id(self):
        return self._route_id

    def get_owner_info(self):
        return BusOwner.get_by_id(self.owner_id)

    @classmethod
    def add(cls, registration_no, owner_id, route_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Buses (RegistrationNo, OwnerID, RouteID) VALUES (?, ?, ?)', (registration_no, owner_id, route_id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''SELECT Buses.*, BusOwner.OwnerFirstName, BusOwner.OwnerLastName
                          FROM Buses
                          JOIN BusOwner ON Buses.OwnerID = BusOwner.OwnerID''')
        buses = cursor.fetchall()
        conn.close()
        return [cls(bus['BusID'], bus['RegistrationNo'], bus['OwnerID'], bus['RouteID']) for bus in buses]

    def update(self, registration_no, owner_id, route_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Buses SET RegistrationNo = ?, OwnerID = ?, RouteID = ? WHERE BusID = ?', (registration_no, owner_id, route_id, self.bus_id))
        conn.commit()
        conn.close()

    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Buses WHERE BusID = ?', (self.bus_id,))
        conn.commit()
        conn.close()
