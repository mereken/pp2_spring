import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    dbname='snake_game',
    user='postgres',
    password='3959'
    )
cur = conn.cursor()

# Create the user table
cur.execute("""
CREATE TABLE IF NOT EXISTS useer (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE
);
""")

# Create the user_score table
cur.execute('''CREATE TABLE IF NOT EXISTS user_score (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                score INTEGER,
                level INTEGER,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(id)
            );
            ''')

conn.commit()
conn.close()
