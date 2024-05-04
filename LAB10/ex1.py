import psycopg2
import csv

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    dbname='phonebook',
    user='postgres',
    password='3959'
    )
cur = conn.cursor()

# Design tables for phonebook
cur.execute("""
CREATE TABLE PhoneBook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL
);
""")

cur.execute("""
INSERT INTO phonebook (username, phone) VALUES
    ('Men', '010102'),
    ('Sen', '010103');
""")

# # Upload data from a csv file
# with open('phonebook_data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if len(row) == 2:
#             username, phone = row
#             cur.execute(f"""INSERT INTO phonebook (username, phone) VALUES (%s, %s);""")


#         # cur.execute(
#         #     "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
#         #     row
#         # )


# Entering user name, phone from console
username = input("Enter username: ")
phone = input("Enter phone number: ")

cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))


# # Implement updating data in the table (change user first name or phone):
# new_username = input("Enter new username: ")
# old_username = input("Enter old username: ")

# cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_username, old_username))


# #Querying data from the tables (with different filters):
# cur.execute("SELECT * FROM phonebook WHERE phone LIKE '555%'")

# rows = cur.fetchall()
# for row in rows:
#     print(row)


# #Implement deleting data from tables by username of phone:
# username = input("Enter username to delete: ")

# cur.execute("DELETE FROM phonebook WHERE username = %s", (username,))



conn.commit()
cur.close()
conn.close()







