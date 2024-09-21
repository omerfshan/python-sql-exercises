import mysql.connector

def getProduct(id):
    connection=mysql.connector.connect(host="localhost",user="root",password="12345678",database="node-app")
    cursor=connection.cursor()
   
    sql="Select * From Products Where id=%s"
    params=(id,)
    cursor.execute(sql,params)
    result= cursor.fetchone()
    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")
    connection.close()
   

getProduct(3)
 