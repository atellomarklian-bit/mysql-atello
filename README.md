# Python MySQL Todo Manager

A command-line Todo application that stores tasks in a MySQL database. It supports adding, viewing, updating, completing, and deleting tasks.

## Project structure

```
main.py       Menu, database readiness check, and application loop
todo.py       Task actions and console output
database.py   MySQL connection and task queries
schema.sql    Creates the todo_db database and tasks table
run.bat       Windows launcher (creates venv, installs driver, runs app)
```

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

## 4. Create the database

The app creates `todo_db` and the `tasks` table automatically on startup. To create them manually, import `schema.sql`:

```bash
mysql -u root -p < schema.sql
```

Or paste the contents of `schema.sql` into phpMyAdmin's SQL tab.

## 5. Run the app

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
python main.py
```

## 6. Use the app

```
1. Add Task
2. View All Tasks
3. View Task by ID
4. Update Task
5. Mark Task as Completed
6. Delete Task
0. Exit
```

Enter a number and follow the prompts.

## Configuration

Connection settings can be set with environment variables. The defaults match a standard XAMPP install:

| Variable      | Default     |
| ------------- | ----------- |
| `DB_HOST`     | `localhost` |
| `DB_USER`     | `root`      |
| `DB_PASSWORD` | *(empty)*   |
| `DB_NAME`     | `todo_db`   |

For example, on macOS/Linux:

```bash
DB_USER=myuser DB_PASSWORD=mypassword python main.py
```

On Windows (Command Prompt):

```bat
set DB_USER=myuser
set DB_PASSWORD=mypassword
python main.py
```
