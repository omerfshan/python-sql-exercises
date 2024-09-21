import mysql.connector

def UpdateProduct(id,name,price):
    connection=mysql.connector.connect(host="localhost",user="root",password="12345678",database="node-app")
    cursor=connection.cursor()
    sql="Update  products Set name=%s,price=%s Where id=%s"
    values=(name,price,id)
    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi")
       
    except mysql.connector.Error as e:
        print("hata",e)
    finally:
        connection.close()
        print("kayıt tamamlandı")

   
UpdateProduct(2,"aaaa",10000)
 