import sqlite3
import pandas as pd

# Assuming you've already installed openpyxl
from openpyxl import Workbook

conn = sqlite3.connect("person_data.db")

df = pd.read_sql_query('select * from person', conn)

# Create an Excel writer object with openpyxl
excel_writer = pd.ExcelWriter("person_table.xlsx", engine='openpyxl')

# Write the DataFrame to the Excel file
df.to_excel(excel_writer, index=False)

# Save the Excel file
excel_writer._save()

# Close the SQLite connection
conn.close()
