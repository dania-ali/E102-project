#############
#Section 1 - Import Modules and Global Variables

import mysql.connector
#############

#############
#Section 2 - Class Definition
#############


#############
#Section 3 - Functions Definition
def greeting():
    def get_user_name():
        return input("Please enter your name: ")
    print("Welcome to Elite Banking System!")
    name = get_user_name()
    print(f"Hello, {name}!")

def display_menu():
    print("\n **Please choose from the following options:**")
    print("1. Check Balance")
    print("2. Deposit Balance")
    print("3. Withdraw Funds")
    print("4. Create New Account")
    print("5. Modify Account")
    print("6. Exit")

def user_selection():
    # Program starts with in_use = True, indicating the program is running
    in_use = True
    while in_use:
        try:
            user_input = int(input("Enter a number between 1-5: "))
            if user_input == 1:
                =
            elif user_input == 2:
                
            elif user_input == 3:
                login_user()
            elif user_input == 4:
                register_user()
            elif user_input == 5:
                print("Goodbye! Thank you for your time!")
                # Exiting the program
                in_use = False
            else:
                print("\nSorry, not a valid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Function to establish a database connection
def create_connection():
    try:
        # Attempt to establish a connection to the database using the specified credentials.
        connection = mysql.connector.connect(
            host="your_host",  # Replace with your database host (e.g., "localhost" or an IP address).
            user="your_user",  # Replace with your username for the database.
            password="your_password",  # Replace with your password for the database.
            database="your_database"  # Replace with the name of the database you're connecting to.
        )
        return connection  # Return the connection object if successful.
    except mysql.connector.Error as error:
        # Handle MySQL-specific errors. 'error' is a variable holding the details of the database error.
        print(f"Error connecting to MySQL: {error}")
        return None  # Return None if the connection fails.

# Function to retrieve the balance of a specific account
def view_balance():
    try:
        # Step 1: Prompt the user to enter their account ID.
        account_id = input("Please enter your account ID: ")

        # Step 2: Establish a connection to the database.
        connection = create_connection()
        if connection:
            # Step 3: Create a cursor object to interact with the database.
            cursor = connection.cursor()

            # Step 4: Define the SQL query to fetch the balance for the given account ID.
            query = "SELECT balance FROM accounts WHERE account_id = %s"
            
            # Step 5: Execute the SQL query, replacing the placeholder (%s) with the provided account ID.
            cursor.execute(query, (account_id,))

            # Step 6: Retrieve the query result (the balance for the account).
            result = cursor.fetchone()

            # Step 7: Close the connection to the database once the operation is complete.
            connection.close()

            # Step 8: Return or display the balance if the account exists; otherwise, show an error message.
            if result:
                # Format the balance to display as a currency with 2 decimal places.
                # `${result[0]:.2f}` ensures that the balance is shown as a float rounded to 2 decimals (e.g., $123.45).
                print(f"Your account balance is: ${result[0]:.2f}")
            else:
                print("Account not found.")
    except Exception as e:
        # Handle any unexpected errors and print an error message.
        # 'Exception' is a general error class, and 'e' is a variable holding the error details.
        print(f"An unexpected error occurred: {e}")


#############

#############
#Section 4 - Running Section
greeting()
display_menu()
user_selection()
#############