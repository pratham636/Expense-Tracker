# Expense Tracker CLI

A Python-based Command Line Interface application to manage and track daily expenses using a MySQL database. 

## 🚀 Features
- **Add Expenses:** Log product names, prices, categories, and dates.
- **Update Records:** Edit any field (name, price, category, or date) by the product ID.
- **Delete Records:** Remove specific entries by ID.
- **Data Summaries:** - View all records.
  - View expenses grouped by category (Total, Average, and Count).
  - Get a high-level summary including total spending and highest expense.

## 🛠️ Technical Setup

### 1. Prerequisites
Ensure you have Python and MySQL installed. You will also need the MySQL connector:
```bash
pip install -r requirement.txt
### 2. Database Configuration
Log into your MySQL server (via MySQL Workbench or Terminal) and run the following commands to set up the table structure. 

> **Note:** The table uses the column name `catagory` to match the spelling in the current Python logic.

```sql
CREATE DATABASE expenses_tracker;

USE expenses_tracker;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    category VARCHAR(255),
    date VARCHAR(50)
);

### 3. Update Credentials
Before running the application, open `database.py` and update the connection parameters with your local MySQL password:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="your_password_here",
    database="expenses_tracker"
)
## 📂 Project Structure

This project follows a modular structure to keep the database logic separate from the user interface:

* **`database.py`**: Manages the connection settings and handles the bridge to your MySQL server.
* **`queries.py`**: Contains all the SQL logic for adding, deleting, updating, and summarizing your expenses.
* **`main.py`**: The entry point of the application. It runs the menu loop and handles all user inputs.

## 🖥️ How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the project folder.
3.  Run the application using:
    ```bash
    python main.py
    ```
