import sys

import mysql.connector

# =====================================================================
# BEGINNER GUIDE: what mysql-connector-python and SQL can do
# =====================================================================
#
# A database stores data in TABLES (like a spreadsheet).
# A table has COLUMNS (fields) and ROWS (records).
#
# --- 1. Connect ------------------------------------------------------
#   db = mysql.connector.connect(host=, user=, password=, database=)
#   db.is_connected()   -> True / False
#   db.close()          -> close the connection
#
# --- 2. Cursor -------------------------------------------------------
#   A cursor runs SQL and reads the results.
#   cursor = db.cursor()
#   cursor = db.cursor(dictionary=True)   # rows as dicts instead of tuples
#
# --- 3. Running SQL --------------------------------------------------
#   cursor.execute(sql, params)     # one statement; params = tuple or dict
#   cursor.executemany(sql, rows)   # same statement for many rows
#   Always use %s placeholders, never f-strings, to avoid SQL injection:
#       cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
#
# --- 4. Reading results ----------------------------------------------
#   cursor.fetchone()      -> next row (or None)
#   cursor.fetchall()      -> list of all remaining rows
#   cursor.fetchmany(n)    -> next n rows
#   cursor.rowcount        -> rows changed by the last INSERT/UPDATE/DELETE
#   cursor.lastrowid       -> id created by the last INSERT
#
# --- 5. Saving changes -----------------------------------------------
#   db.commit()     -> save (required for INSERT / UPDATE / DELETE)
#   db.rollback()   -> undo uncommitted changes
#
# --- 6. Common SQL commands ------------------------------------------
#   CREATE DATABASE test_db;
#   USE test_db;
#   CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));
#   INSERT INTO users (name) VALUES ('Alice');
#   SELECT * FROM users;
#   SELECT id, name FROM users WHERE id = 1;
#   UPDATE users SET name = 'Bob' WHERE id = 1;
#   DELETE FROM users WHERE id = 1;
#   DROP TABLE users;               -- deletes the whole table
#
# --- 7. Helpful extras -----------------------------------------------
#   CREATE TABLE IF NOT EXISTS ...  -- no error if the table already exists
#   ALTER TABLE users ADD email VARCHAR(100);
#   SELECT COUNT(*) FROM users;
#   ORDER BY name [ASC|DESC]        -- sort rows
#   LIMIT 10                        -- return only 10 rows
# =====================================================================

HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "kenpydev"
TABLE = "users"

try:
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
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
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
cursor.execute(f"USE {DATABASE}")

cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")

while True:
    print("\n1. Add user")
    print("2. Delete user")
    print("3. Show users")
    print("4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        cursor.execute(f"INSERT INTO {TABLE} (name) VALUES (%s)", (name,))
        db.commit()
        print("Saved!")

    elif choice == "2":
        cursor.execute(f"SELECT id, name FROM {TABLE}")
        rows = cursor.fetchall()
        for i, row in enumerate(rows, start=1):
            print(i, row[1])
        n = int(input("Number to delete: "))
        cursor.execute(f"DELETE FROM {TABLE} WHERE id = %s", (rows[n - 1][0],))
        db.commit()
        print("Deleted!")

    elif choice == "3":
        cursor.execute(f"SELECT id, name FROM {TABLE}")
        for i, row in enumerate(cursor.fetchall(), start=1):
            print(i, row[1])

    elif choice == "4":
        break

db.close()
