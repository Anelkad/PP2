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
    name = 'A'
    new_id = '4'
    cur.execute(sql, (new_id,name))
    print(cur.rowcount)


def querying():
    sql = """
    SELECT * FROM students WHERE gpa>3.00
    """
    cur.execute(sql)

    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()

def deleting(cur):
    sql = """
    DELETE FROM students WHERE gpa<2.0
    """
    cur.execute(sql)

    print(cur.rowcount)

querying()
cur.close()
conn.commit()