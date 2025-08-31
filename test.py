import pymysql

conn = None
cursor = None

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',        
        password='abisheek',    
        database='library_db'
    )
    
    print("Connected to MySQL database")

    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db = cursor.fetchone()
    print(f"Using database: {db[0]}")

    cursor.execute("SELECT * FROM library_management LIMIT 5;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except pymysql.MySQLError as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
        print("MySQL connection closed")
