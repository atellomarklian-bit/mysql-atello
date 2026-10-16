import sys

import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
    )
except mysql.connector.Error as err:
    print("ERROR: Not connected to MySQL.")
    print(f"Reason: {err}")
    print("Make sure MySQL is running in XAMPP and the settings in database.py are correct.")
    sys.exit(1)

if db.is_connected():
    print("Connected to MySQL successfully.")
else:
    print("ERROR: Not connected to MySQL.")
    sys.exit(1)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
cursor.execute("USE test_db")

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")

while True:
    print("\n1. Add user")
    print("2. Delete user")
    print("3. Show users")
    print("4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        db.commit()
        print("Saved!")

    elif choice == "2":
        cursor.execute("SELECT id, name FROM users")
        rows = cursor.fetchall()
        for i, row in enumerate(rows, start=1):
            print(i, row[1])
        n = int(input("Number to delete: "))
        cursor.execute("DELETE FROM users WHERE id = %s", (rows[n - 1][0],))
        db.commit()
        print("Deleted!")

    elif choice == "3":
        cursor.execute("SELECT id, name FROM users")
        for i, row in enumerate(cursor.fetchall(), start=1):
            print(i, row[1])

    elif choice == "4":
        break

db.close()
