import psycopg2

#connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='suppliers', 
    user='postgres', 
    password='3959' 
    )
#create a cursor to work with the database
cur = conn.cursor()

#querying the database
cur.execute('SELECT Version()')

db_ver = cur.fetchall()

print(db_ver)




