#############
#Section 1 - Import Modules and Global Variables
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


def register_user():
    username = input("Enter a username: ")
    if username in usernames:
        print("Username already exists. Please choose another.")
        return
    password = input("Enter a password: ")
    usernames.append(username)
    passwords.append(password)
    print("Registration successful!")

def login_user():
    global is_logged_in
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in usernames:
        index = usernames.index(username)
        if passwords[index] == password:
            print("Login successful!")
            is_logged_in = True
            return
    print("Invalid username or password.")
#############

#############
#Section 4 - Running Section
greeting()
display_menu()
user_selection()
#############