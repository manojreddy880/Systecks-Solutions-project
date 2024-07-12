import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('StudentsPerformance.db')
cursor = conn.cursor()

print("Filter by Gender:")
cursor.execute("SELECT * FROM performance WHERE gender = 'female'")
female_students = cursor.fetchall()  # Fetch all rows that match the query

for student in female_students:
    print(student)  # Adjust print statement as needed based on your database schema

# Operation 2: Aggregate Scores by Race/Ethnicity
print("\nAggregate Scores by Race/Ethnicity:")
cursor.execute("""
SELECT race_ethnicity, 
       AVG(math_score) AS avg_math_score,
       AVG(reading_score) AS avg_reading_score,
       AVG(writing_score) AS avg_writing_score
FROM performance
GROUP BY race_ethnicity
""")
aggregated_scores = cursor.fetchall()
for row in aggregated_scores:
    print(row)

# Operation 3: Count Students by Parental Level of Education
print("\nCount Students by Parental Level of Education:")
cursor.execute("""
SELECT parental_level_of_education, COUNT(*) AS student_count
FROM performance
GROUP BY parental_level_of_education
""")
student_counts = cursor.fetchall()
for row in student_counts:
    print(row)

# Operation 4: Compare Scores Between Students with Standard and Free/Reduced Lunch
print("\nCompare Scores Between Students with Standard and Free/Reduced Lunch:")
cursor.execute("""
SELECT lunch, 
       AVG(math_score) AS avg_math_score,
       AVG(reading_score) AS avg_reading_score,
       AVG(writing_score) AS avg_writing_score
FROM performance
GROUP BY lunch
""")
lunch_comparison = cursor.fetchall()
for row in lunch_comparison:
    print(row)

# Operation 5: Identify Top Performers (Top 10% by Average Score)
print("\nTop Performers (Top 10% by Average Score):")
cursor.execute("""
SELECT *, (math_score + reading_score + writing_score) / 3.0 AS average_score
FROM performance
ORDER BY average_score DESC
LIMIT (SELECT COUNT(*) / 10 FROM performance)
""")
top_performers = cursor.fetchall()
for student in top_performers:
    print(student)

# Close connection
conn.close()
