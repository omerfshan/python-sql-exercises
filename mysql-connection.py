import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678"
    
)

mycursor=mydb.cursor()

mycursor.execute("Show Databases")

for i in mycursor:
    print(i)