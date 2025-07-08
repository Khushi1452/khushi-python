import sqlite3
connection=sqlite3.connect("School.db") 
cur=connection.cursor()

#cur.execute("CREATE TABLE student(id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
#cur.execute("CREATE TABLE marks(student_id INTEGER, total_marks INTEGER, grade TEXT)")

cur.execute("INSERT INTO student VALUES(3, 'Gursimra', 'g123@gmail.com')")
cur.execute("INSERT INTO student VALUES(4, 'Vikas', 'v123@gmail.com')")

cur.execute("INSERT INTO marks VALUES(1, 800, 'A')")
cur.execute("INSERT INTO marks VALUES(2, '550', 'B')")
cur.execute('SELECT *FROM student')
rows = cur.fetchall()
for row in rows:
    print(rows)
connection.commit()
connection.close()
