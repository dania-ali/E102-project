import sqlite3

#database name
DB_NAME = 'student.db'


def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students
            (id integer primary key, 
            name text, 
            age integer, 
            grade text, 
            gpa real)
    ''')

    print("Table created.")

    # Insert sample data
    print("Inserting sample data...")
    create_user(cursor, 'Evan', 16, '11', 4.0)
    # cursor.execute('''
    #     INSERT INTO students (name, age,grade, gpa) VALUES
    #     ('Alice', 16, '10th', 3.5),
    #     ('Bob', 17, '11th', 3.8),
    #     ('Charlie', 15, '9th', 3.2),
    #     ('Zac', 28, '10th', 3.2)
    # ''')

    print("\n--- Querying Specific Columns (Name and Age) ---")
    cursor.execute("SELECT name, age FROM students")
    name_age = cursor.fetchall()
    for row in name_age:
        print(f"Name: {row[0]}, Age: {row[1]}")
    print("Sample data inserted.")
    # Commit the changes and close the connection
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()

def create_user(cursor, name, age, grade, gpa):
  cursor.execute('''
        INSERT INTO students (name, age, grade, gpa) VALUES (?, ?, ?, ?)
    ''', (name, age, grade, gpa))


initialize_database()