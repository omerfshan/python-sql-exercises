import mysql.connector

def getProductInfo():
    connection=mysql.connector.connect(host="localhost",user="root",password="12345678",database="node-app")
    cursor=connection.cursor()
   
    sql="Select COUNT(*) from Products"
    sql="Select AVG(Price) from Products"
    sql="Select SUM(Price) from Products"
    sql="Select MIN(Price) from Products"
    sql="Select MAX(Price) from Products"
    sql="Select Name,Price from Products Where Price=(Select MAX(Price) from Products)"



    cursor.execute(sql)
    result= cursor.fetchone()
    
    print(f"RESULT : {result[0]}")
    connection.close()
   
getProductInfo()
 