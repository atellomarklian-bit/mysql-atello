# MySQL Python CRUD (XAMPP)

A simple command-line Python app that connects to MySQL (via XAMPP) and lets you add, delete, and view users in a `users` table.

## 1. Clone this repo

```bash
git clone https://github.com/ken-py-dev/mysql.git
cd mysql
```

## 2. Set up XAMPP

1. Download and install XAMPP: https://www.apachefriends.org/
2. Open the **XAMPP Control Panel**.
3. Start the **MySQL** module (click **Start**).
   - Optional: start **Apache** if you want phpMyAdmin.
4. By default MySQL runs on `localhost` port `3306` with:
   - user: `root`
   - password: *(empty)*
5. (Optional) Verify in the browser at http://127.0.0.1/phpmyadmin

## 3. Install Python

1. Download and install Python 3: https://www.python.org/downloads/
2. During install, check **"Add Python to PATH"**.
3. Verify:
   ```bash
   python --version
   ```

## 4. Run the Python app

### Windows (automatic)

Double-click `run.bat`, or run from the project folder:

```bash
run.bat
```

The script creates a virtual environment, installs the driver, and starts the app.

### Manual (Windows / macOS / Linux)

```bash
python -m venv venv
```

Activate the virtual environment:

- Windows: `venv\Scripts\activate`
- macOS / Linux: `source venv/bin/activate`

Install the MySQL driver and run:

```bash
pip install mysql-connector-python
python database.py
```

## 5. Use the app

```
1. Add user
2. Delete user
3. Show users
4. Exit
```

Enter a number and follow the prompts. Data is stored in the `test_db` database, `users` table.

## Configuration

Connection settings are in `database.py`:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)
```

Change `host`, `user`, or `password` to match your XAMPP MySQL setup.
