import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    dbname='phonebook',
    user='postgres',
    password='3959'
    )
cur = conn.cursor()

#Delete table
cur.execute('DROP TABLE phonebook;')
conn.commit()

# Design tables for phonebook
cur.execute("""
CREATE TABLE PhoneBook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
);
""")

import csv
with open('phonebook_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)

        username, phone = row
        cur.execute(f"""INSERT INTO contacts2 (username, phone) VALUES ('{username}','{phone}');""")

conn.commit()

cur.execute("""
INSERT INTO students_data (name, id, study_year, phone_number) VALUES
    ('Haru', '010102'),
    ('Dano', '010103');
""")
 

# # Entering user name, phone from console
# user_name = input("Enter username: ")
# phone = input("Enter phone number: ")

# cur.execute("INSERT INTO PhoneBook (user_name, phone) VALUES (%s, %s)", (user_name, phone))

# conn.commit()






