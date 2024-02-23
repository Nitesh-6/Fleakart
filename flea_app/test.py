import mysql.connector

myconn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'tiger', database = 'ecomm_db')
cursor = myconn.cursor()
cursor.execute("SELECT * FROM products")
num_rows = 9
while True:
    rows = cursor.fetchmany(size = num_rows)
    if not rows:
        break
    for row in rows:
        print(row)