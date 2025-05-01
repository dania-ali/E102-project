import sqlite3

#database name
DB_NAME = "bank.db"

def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a users table
    print("Creating users table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             username TEXT UNIQUE, 
             password TEXT, 
             balance REAL DEFAULT 0.0)
    ''')

    # Insert a sample user
    print("Inserting sample data...")
    create_user(cursor, 'Evan', 'password123', 100.0)

    # Save changes and close the connection
    connection.commit()
    print("Database changes committed.")
    connection.close()
    print("Database connection closed.\n")


#Insert user into table
def create_user(cursor, username, password, balance = 0.0):
    #insert a new user into the users table
    cursor.execute(INSERT INTO users (username, password, balance) VALUES (?, ?, ?)", 
                    (username, password, balance))
    print(" User {username} added.")

initialize_database()