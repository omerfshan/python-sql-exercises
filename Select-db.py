import mysql.connector

def getProduct():
    connection=mysql.connector.connect(host="localhost",user="root",password="12345678",database="node-app")
    cursor=connection.cursor()
    # cursor.execute("Select*From Products")
    cursor.execute("Select name,price From Products")
    result= cursor.fetchall()
    # result= cursor.fetchone()
    # print(f"{result[0]} {result[1]}")
    for i in result:
      print(f"{i[0]} {i[1]}")

getProduct()
 