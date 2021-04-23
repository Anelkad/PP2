import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="tsis",
    user="postgres",
    password="16anel16")
cur = conn.cursor()

#cur.execute(""" 
#CREATE TABLE students (
#  id      VARCHAR(10),
#  name    VARCHAR(255),
#  faculty VARCHAR(255),
#  gpa     NUMERIC
#);
#""")

#sql = """
#INSERT INTO students VALUES ('1','A','FIT',3.0),
#('2','B','FIT',2.5),
#('3','C','BS',4.0);"""
#cur.execute(sql)

#sql = """
#UPDATE students SET id=%s WHERE name=%s
#"""
#name = 'A'
#new_id = '4'
#cur.execute(sql, ( new_id,name))
#print(cur.rowcount)

#sql = """
#SELECT * FROM students
#"""
#cur.execute(sql)

#row = cur.fetchone()

#while row is not None:
#    print(row)
#    row = cur.fetchone()

sql = """
DELETE FROM students WHERE gpa<3.0
"""
cur.execute(sql)

print(cur.rowcount)


cur.close()
conn.commit()