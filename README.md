# Export-SQL-Table-to-Excel-with-Python

## Fake Person Data Generator and SQLite to Excel Export

This repository contains a Python script that uses the Faker library to generate fake person data and store it in an SQLite database. The script then retrieves the data from the SQLite database, creates a Pandas DataFrame, and exports it to an Excel file using the openpyxl library.

## Overview
### generate_fake_data.py: 
This script creates an SQLite database (person_data.db) and a table (person) to store fake person data. It uses the Faker library to generate random names, ages, addresses, phone numbers, and emails for 500 individuals. The generated data is then inserted into the SQLite database.

## export_to_excel.py: 
This script reads the data from the SQLite database into a Pandas DataFrame and exports it to an Excel file (person_table.xlsx). The export process is facilitated by the openpyxl library.

# Dependencies
## sqlite3: Python's SQLite library for database interaction.
## Faker: A Python library for generating fake data.
## pandas: A powerful data manipulation library.
## openpyxl: A library for reading and writing Excel files.
How to Use
Install the required dependencies:

bash
Copy code
## pip install sqlite3 Faker pandas openpyxl
Run the generate_fake_data.py script to generate and store fake person data in the SQLite database.

bash
Copy code
python generate_fake_data.py
Run the export_to_excel.py script to export the data to an Excel file.

bash
Copy code
python export_to_excel.py
