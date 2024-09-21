import mysql.connector

def DeleteProduct(id):
    connection=mysql.connector.connect(host="localhost",user="root",password="12345678",database="node-app")
    cursor=connection.cursor()
    sql="delete from products where id=%s "
    values=(id,)
    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt silindi")
       
    except mysql.connector.Error as e:
        print("hata",e)
    finally:
        connection.close()
        

   
DeleteProduct(2)
 