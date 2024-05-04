# Framework: psycopg2
import psycopg2
# Connect to the database by creating a connection object
conn = psycopg2.connect(
    dbname='students',
    user='postgres',
    password='3959'
)


# Create a cursor to work with the database
cur = conn.cursor()

#Delete table
cur.execute('DROP TABLE students_data;')
conn.commit()


# Creatw a new table
cur.execute("""
CREATE TABLE students_data (
    name VARCHAR(255),
    id VARCHAR(255) PRIMARY KEY,
    study_year INT,
    phone_number VARCHAR(20)
);
""")

# Create new students
cur.execute("""
INSERT INTO students_data (name, id, study_year, phone_number) VALUES
    ('Ruslan', '24BD202424', 1, '+77007007070'),
    ('Mariya', '24BD202425', 1, '+77077077070');
""")

# Update students
cur.execute("""
    UPDATE students_data
    SET study_year = 2
    WHERE name = 'Ruslan';
""")

# Delete students
cur.execute("""
    DELETE FROM students_data
    WHERE name = 'Ruslan';
""")


conn.commit()


















import csv

filename = "labwork10/first/2/contactname.csv"

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)

        name, phone_number = row
        
        cur.execute(f"""INSERT INTO contacts2 (name, phone_number) VALUES ('{name}','{phone_number}');""")

conn.commit()
