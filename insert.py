import mysql.connector

def insertProduct(name,price,imageUrl,description):
    connection=mysql.connector.connect(host="localhost",user="root",password="12345678",database="node-app")
    cursor=connection.cursor()
    sql="INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values=(name,price,imageUrl,description)
    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id{cursor.lastrowid}")
    except mysql.connector.Error as e:
        print("hata",e)
    finally:
        connection.close()
        print("kayıt tamamlandı")


def insertProducts(list):
    connection=mysql.connector.connect(host="localhost",user="root",password="12345678",database="node-app")
    cursor=connection.cursor()
    sql="INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values=list
    cursor.executemany(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id{cursor.lastrowid}")
    except mysql.connector.Error as e:
        print("hata",e)
    finally:
        connection.close()
        print("kayıt tamamlandı")
list=[]
while True:
    name=input("ürün adi: ")
    price=float(input("ürün fiyati: "))
    imageUrl=input("ürün resmi: ")
    description=input("açıklama: ")
    list.append((name,price,imageUrl,description))
    result=input("devam etmek istiyormusunuz (e/h)")
    if result=="h":
        print("kayıtlar veri tabanına aktarılıyor...")
        insertProducts(list)

