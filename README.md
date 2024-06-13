# Bus Sacco Management App

This Bus Sacco Management App is a command-line application designed to manage bus owners, buses, and routes for a bus company. It allows users to perform various operations such as adding, viewing, updating, and deleting bus owners, buses, and routes.

## Features

- Add, view, update, and delete bus owners.
- Add, view, update, and delete buses along with their owners and routes.
- Add, view, update, and delete routes.

## Prerequisites

Python 3.x installed on your system
SQLite database installed on your system

## Installation and Setup

1. **Clone the repository:**
   git clone <https://github.com/Mosh9098/Phase3-Bus-Company-Proj.git>

2. **Navigate to project directory:**
cd your_project

3. **Install dependencies: (Ensure you have Python and pip installed):**
pipenv install
pipenv shell

4. **Initialize the database: (This will create necessary tables)**
python db/setup.py

**USAGE:Run the CLI script to start the application:**
python cli.py

## Database

The app uses a SQLite database to store bus owners, buses, and routes. The database is located in the db directory, and the database file is named BusCompany.db.

## License

This project is licensed under the MIT License.
