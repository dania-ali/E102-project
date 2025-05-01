#############
#Section 1 - Import Modules and Global Variables
import sqlite3
#############

#############
#Section 2 - Class Definition
#############


#############
#Section 3 - Functions Definition

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

    # Save changes and close the connection
    connection.commit()
    print("Database changes committed.")
    connection.close()
    print("Database connection closed.\n")


#Handle user registration
def register_user():
    #Database connection
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    #Ask for login info
    print("\n--- User Registration ---")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    #Insert new user into database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    connection.commit()
    print("✅ Account successfully created!")

    #closing connection
    connection.close()


#User login function
def login_user():
    #Database connection
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    #Ask for login info
    print("\n--- User Login ---")
    username = input("Username: ")
    password = input("Password: ")

    #Does user exist?
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    connection.close()

    #User data if successful login
    if user:
        print(f"✅ Login successful. Welcome, {username}!")
        return user
    else:
        print("❌ Login failed. Please check your credentials.")
        return None

#Display menu after login
def display_menu():
    print("\n --- Main Menu ---")
    print("1️⃣  Check Balance")
    print("2️⃣  Deposit Funds")
    print("3️⃣  Withdraw Funds")
    print("4️⃣  Modify Account")
    print("5️⃣  Close Account")
    print("6️⃣  Logout")

#Check user balance
def check_balance(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    balance = cursor.fetchone()[0]
    #shows 2 decimal places
    print(f"💰 Your current balance is: ${balance:.2f}")
    connection.close()

def deposit(user_id):
    #ask how much to deposit
    amount = float(input("Enter deposit amount:"))

    #Update balance
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, user_id))
    connection.commit()
    print(f"✅ ${amount:.2f} deposited successfully.")
    connection.close()

#Withdraw funds
def withdraw(user_id):
    #ask how much to withdraw
    amount = float(input("Enter withdrawal amount: "))

    #get current balance
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    current_balance = cursor.fetchone()[0]

    #check if theres enough before withdrawing
    if amount > current_balance:
        print("❌ Insufficient funds.")
    else:
        cursor.execute("UPDATE users SET balance = balance - ? WHERE id = ?", (amount, user_id))
        connection.commit()
        print(f"✅ ${amount:.2f} withdrawn successfully.")
    connection.close()

#modify account
def modify_account(user_id):
    # database connection
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    #ask user what to change
    print("\n--- Modify Account ---")
    print("1. Change Username")
    print("2. Change Password")
    choice = input("Select an option to modify: ")

    if choice == '1':
        # Modify the username
        new_username = input("Enter the new username: ")
        cursor.execute("UPDATE users SET username = ? WHERE id = ?", (new_username, user_id))
        print(f"✅ Username updated to {new_username}.")
    elif choice == '2':
        # Modify the password
        new_password = input("Enter the new password: ")
        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, user_id))
        print("✅ Password updated.")
    else: 
        print("❌ Invalid option. No changes made.")

    # Commit changes and close connection
    connection.commit()
    connection.close()

#account closure function
def close_account(user_id):
    # Database connection
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Ask the user to confirm 
    confirmation = input("Are you sure you want to close your account? This action is permanent (y/n): ")

    if confirmation.lower() == 'y':
        # Delete account from database
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        print("❌ Account deleted permanently.")
    else:
        print("🚫 Account closure canceled.")

    # Commit changes and close connection
    connection.commit()
    connection.close()

#menu after logging in
def user_selection(user):
    while True:
        #show menu
        display_menu()
        choice = input("Select an option (1-6): ")
        
        if choice == '1':
            check_balance(user[0])
        elif choice == '2':
            deposit(user[0])
        elif choice == '3':
            withdraw(user[0])
        elif choice == '4':
            modify_account(user[0])
        elif choice == '5':
            close_account(user[0])
            break  # Exit the session after account closure
        elif choice == '6':
            print("👋 Logging out...")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")

#Main program
def main():
    #intialize database w/ table
    initialize_database()
    print("🏦 Welcome to Elite Banking System!")

    #show login menu
    while True:
        print("\n--- Start Menu --- ")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        # Ask the user what they want to do
        choice = input("Choose an option: ")

        # If login, go to session
        if choice == '1':
            user = login_user()
            if user:
                user_selection(user)
        # If register, go to registration
        elif choice == '2':
            register_user()
        # Exit program
        elif choice == '3':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid input. Please try again.")
#############

#############
#Section 4 - Running Section
main()
#############