import sqlite3
conn = sqlite3.connect("demo.db")
print("opened database successfully")
conn.execute("CREATE TABLE raj (username varchar,email varchar,password varchar,phone varchar)")
conn.execute("CREATE TABLE bookings(name varchar,phone number,email varchar,person varchar)")
print("table created successfully")
conn.close()
