import psycopg2

connect = psycopg2.connect("dbname=crud user=postgres password=mynewpassword host=localhost")

cursor = connect.cursor()
cursor.execute("SELECT * FROM person;")
records = cursor.fetchall()
print(records)
