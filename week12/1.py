import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="tsis",
    user="postgres",
    password="16anel16")
cur = conn.cursor()

def createtable():
    cur.execute(""" 
    CREATE TABLE students (
    id      VARCHAR(10),
    name    VARCHAR(255),
    faculty VARCHAR(255),
    gpa     NUMERIC
    );
    """)

def inserting():
    sql = """
    INSERT INTO students VALUES
    ('4','D','BS',1.5),
    ('5','E','FIT',2.0);
    """
    cur.execute(sql)

def updating():
    sql = """
    UPDATE students SET id=%s WHERE name=%s
    """
    name = input("write name ")
    new_id = input("write new id for him ")
    cur.execute(sql, (new_id,name))
    print(cur.rowcount)


def querying():
    print("please write what do you find: id / name / faculty / gpa")
    t=input()
    q=input()
    if t=='gpa':
        sql = "SELECT * FROM students WHERE gpa"+q
    else:
        sql = "SELECT * FROM students WHERE "+t+" = "+"'"+q+"'"
    
    cur.execute(sql)

    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()

def deleting():
    print("please write what do you delete: id / name / faculty / gpa")
    t=input()
    q=input()
    if t=='gpa':
        sql = "DELETE FROM students WHERE gpa"+q
    else:
        sql = "DELETE FROM students WHERE "+t+" = "+"'"+q+"'"
    cur.execute(sql)

    print(cur.rowcount)

deleting()
cur.close()
conn.commit()