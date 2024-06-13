from db.connection import get_db_connection

class Route:
    def __init__(self, route_id, route_name):
        # Initialize the Route instance with the provided attributes
        self._route_id = route_id
        self._route_name = route_name

    def __repr__(self):
        # Define the string representation of the Route instance
        return f'<Route {self.route_name}>'

    # Define the route_id property with a getter method
    @property
    def route_id(self):
        return self._route_id

    # Define the route_name property with a getter method
    @property
    def route_name(self):
        return self._route_name

    # Define the setter method for the route_name property
    @route_name.setter
    def route_name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Route name must be a non-empty string")
        self._route_name = value

    # Define a class method to add a new Route to the database
    @classmethod
    def add(cls, route_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Routes (RouteName) VALUES (?)', (route_name,))
        conn.commit()
        conn.close()

    # Define a class method to retrieve all Route instances from the database
    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Routes')
        routes = cursor.fetchall()
        conn.close()
        return [cls(route['RouteID'], route['RouteName']) for route in routes]

    # Define an instance method to update the current Route's information in the database
    def update(self, route_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Routes SET RouteName = ? WHERE RouteID = ?', (route_name, self.route_id))
        conn.commit()
        conn.close()

    # Define an instance method to delete the current Route from the database
    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Routes WHERE RouteID = ?', (self.route_id,))
        conn.commit()
        conn.close()
