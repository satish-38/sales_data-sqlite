# Sales Data Analysis with SQLite, Pandas, and Matplotlib

This project demonstrates how to work with sales data stored in an SQLite database. The workflow includes creating a database, inserting sample data, querying with SQL, analyzing using Pandas, and visualizing insights with Matplotlib.

## Features

- Create and connect to a SQLite database
- Create and populate a `sales` table
- Use SQL queries to summarize data (e.g., total quantity, revenue)
- Import SQL query results into Pandas DataFrames
- Visualize top 5 products by revenue using a pie chart
- Save processed data as CSV or Excel files

## Technologies Used

- Python
- SQLite3
- Pandas
- Matplotlib
- Jupyter Notebook
  import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

sales_data = [
    ("samsung", 10, 20000),
    ("apple", 9, 40000),
    ("vivo", 11, 25000),
    ("nokia", 19, 15000),
    ("realme", 5, 10000),
    ("nothing", 6, 24000),
    ("redmi", 10, 27000),
    ("oppo", 12, 23000),
    ("one plus", 13, 23000)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sales_data)
conn.commit()

## Getting Started

1. **Install Required Libraries**

```bash
pip install pandas matplotlib openpyxl
