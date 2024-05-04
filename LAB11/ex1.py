import psycopg2

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
    phone VARCHAR(255) NOT NULL
);
""")

cur.execute("""
INSERT INTO phonebook (username, phone) VALUES
    ('Haru', '010102'),
    ('Dano', '010103'), 
    ('Jay', '010104');
""")

# # Upload data from a csv file
# with open('phonebook_data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         cur.execute(
#             "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
#             row
#         )


# # Entering user name, phone from console
# username = input("Enter username: ")
# phone = input("Enter phone number: ")

# cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))


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

# #Function to return all records based on a pattern:
# cur.execute("""
# CREATE FUNCTION searchPhonebook(pattern VARCHAR(255))
# RETURNS TABLE (name VARCHAR(255), phone_number VARCHAR(20)) 
# AS $$
# BEGIN
#     RETURN QUERY SELECT name, phone_number FROM PhoneBook WHERE name LIKE '%' || pattern || '%' OR phone_number LIKE '%' || pattern || '%';
# END;
# $$ LANGUAGE plpgsql;
# """)


# # Procedure to insert new user and update phone if user already exists:
# cur.execute("""
# CREATE PROCEDURE insertOrUpdateUser(username VARCHAR(255), phone VARCHAR(255))
# AS $$
# BEGIN
#     IF EXISTS (SELECT 1 FROM phobebook WHERE username = username) THEN
#         UPDATE phonebook SET phone = phone 
#         WHERE username = username;
#     ELSE
#         INSERT INTO phonebook (username, phone) VALUES (username, phone);
#     END IF;
# END;
# $$ LANGUAGE plpgsql;

# """)


# #Procedure to insert many new users by list of name and phone:
# cur.execute("""
# CREATE PROCEDURE insertMultipleUsers(users_list JSON)
# AS

# DECLARE
#     user_record JSON;
#     user_name VARCHAR(255);
#     user_phone VARCHAR(20);
# BEGIN
#     FOREACH user_record IN ARRAY users_list
#     LOOP
#         user_name := user_record->>'username';
#         user_phone := user_record->>'phone';
        
#         IF LENGTH(user_phone) != 10 OR NOT user_phone ~ '[0-9]' THEN
#             RAISE EXCEPTION 'Incorrect phone number: %', user_phone;
#         ELSE
#             INSERT INTO phonebook (username, phone) VALUES (user_name, user_phone);
#         END IF;
#     END LOOP;
# END; 

# """)


# Procedure to delete data by username or phone:
cur.execute("""
CREATE PROCEDURE deletePhonebookData(identifier VARCHAR(255))
AS $$
BEGIN
    DELETE FROM phonebook WHERE username = identifier OR phone = identifier;
END;
$$ LANGUAGE plpgsql;

""")






conn.commit()
cur.close()
conn.close()


