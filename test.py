# test.py
import main  # import functions from main.py
import sqlite3

# Setup
main.create_table()
main.create_user("testuser", "pass123", 100.0)
print("User created.")

# Connect to test
connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

# Check if user exists
cursor.execute("SELECT * FROM users WHERE username = ?", ("testuser",))
user = cursor.fetchone()

if user:
    print("Login works ✅")
else:
    print("Login failed ❌")

# Deposit
cursor.execute("UPDATE users SET balance = balance + ? WHERE username = ?", 
               (50.0, "testuser"))
connection.commit()
print("Deposited $50.")

# Check balance
cursor.execute("SELECT balance FROM users WHERE username = ?", ("testuser",))
balance = cursor.fetchone()[0]
print("New balance:", balance)  # Should print 150.0

# Withdraw
cursor.execute("UPDATE users SET balance = balance - ? WHERE username = ?", 
               (30.0, "testuser"))
connection.commit()
cursor.execute("SELECT balance FROM users WHERE username = ?", ("testuser",))
balance = cursor.fetchone()[0]
print("Balance after withdrawal:", balance)  # Should print 120.0

# Close account
cursor.execute("DELETE FROM users WHERE username = ?", ("testuser",))
connection.commit()
print("Account closed.")


connection.close()