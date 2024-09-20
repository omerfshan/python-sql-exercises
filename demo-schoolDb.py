import mysql.connector

connection=mysql.connector.connect(
     host="localhost",
    user="root",
    password="12345678",
    
)
mycursor=connection.cursor()

mycursor.execute("Show Databases")

for i in mycursor:
    print(i)