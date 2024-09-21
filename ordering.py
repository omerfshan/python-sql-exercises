import mysql.connector

def getOrdering():
    connection=mysql.connector.connect(host="localhost",user="root",password="12345678",database="node-app")
    cursor=connection.cursor()
   
    sql="Select * From Products Order By name,price ASC"
    cursor.execute(sql)
    results= cursor.fetchall()
    for result in results: 
        print(f"id: {result[0]} name: {result[1]} price: {result[2]}")
    connection.close()
   
getOrdering()
 