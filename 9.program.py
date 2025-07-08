import sqlite3

connection = sqlite3.connect("company.db") 
cur = connection.cursor()

cur.execute("DROP TABLE IF EXISTS user")
cur.execute("DROP TABLE IF EXISTS information")

# Create tables
cur.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
cur.execute("CREATE TABLE information(user_id INTEGER, salary TEXT)")

# Insert data into student table
cur.execute("INSERT INTO user VALUES(1, 'Khushi', 'khushi456@gmail.com')")
cur.execute("INSERT INTO user VALUES(2, 'Taran', 'taran456@gmail.com')")

# Insert data into marks table
cur.execute("INSERT INTO information VALUES(1, 12000)")
cur.execute("INSERT INTO information VALUES(2, 12000)")  



cur.execute('SELECT *FROM user')
rows=cur.fetchall()
for row in rows:
    print(rows)
connection.commit()
connection.close()