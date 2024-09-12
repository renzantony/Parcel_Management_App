import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('parcels.db')

# Create a cursor object
cursor = conn.cursor()

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Close the connection
conn.close()
