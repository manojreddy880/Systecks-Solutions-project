import csv
import sqlite3

# Path to the CSV file
csv_file_path = 'StudentsPerformance.csv'

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('StudentsPerformance.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS performance (
    gender TEXT,
    race_ethnicity TEXT,
    parental_level_of_education TEXT,
    lunch TEXT,
    test_preparation_course TEXT,
    math_score INTEGER,
    reading_score INTEGER,
    writing_score INTEGER
)
''')

# Read CSV file and insert data into the table
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Skip header row
    for row in reader:
        cursor.execute('''
        INSERT INTO performance (gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, math_score, reading_score, writing_score)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)

# Commit changes and close connection
conn.commit()
conn.close()
