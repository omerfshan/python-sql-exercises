from connection import connection
import mysql.connector
from datetime import datetime
class Student:
    connection=connection
    mycursor=connection.cursor()
    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id=0
        else:
            self.id=id
        
        self.studentNumber=studentNumber
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.gender=gender
    
    def saveStudent(self):
        sql="INSERT INTO Students(StudentNumber,Name,SurName,Birthdate,Genger) VALUES (%s,%s,%s,%s,%s)"
        values=(self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,values)
        try:
            Student.connection.commit()
        except mysql.connector.eror as err:
            print("hata")
        finally:
            Student.connection.close()
    
    @staticmethod
    def saveStudents(liste):
        sql="INSERT INTO Students(StudentNumber,Name,SurName,Birthdate,Genger) VALUES (%s,%s,%s,%s,%s)"
        values=liste
        Student.mycursor.executemany(sql,values)
        try:
            Student.connection.commit()
        except mysql.connector.eror as err:
            print("hata")
        finally:
            Student.connection.close()

    @staticmethod
    def Studentsİnfo():
        sql="Select * from students "
        
        Student.mycursor.execute(sql)
        try:
            results=Student.mycursor.fetchall()
            for result in results:
                print(result)
        except mysql.connector.eror as err:
            print("hata")
        finally:
            Student.connection.close()
   
    @staticmethod
    def getStudentById(id):
        sql="Select * from students where id=%s"
        value=(id,)
        Student.mycursor.execute(sql,value)
        try:
            result= Student.mycursor.fetchone()
            return Student(result[0],result[1],result[2],result[3],result[4],result[5])
        except mysql.connector.eror as err:
            print("hata")
       
    
    def UpdateStudent(self):
       sql = "Update students set StudentNumber=%s, Name=%s, SurName=%s, Birthdate=%s, Genger=%s where id=%s"
       value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender, self.id)
    
       try:
           Student.mycursor.execute(sql, value)
           Student.connection.commit()
       except mysql.connector.Error as err:
          print(f"Hata: {err}")

        
        
    
# ahmet=Student("101", "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E")
# ahmet.saveStudent()
obj=Student.getStudentById(1)
obj.name="ali"
obj.UpdateStudent()
print(obj)
# Student.Studentsİnfo()
ogrenciler=[
    ("309", "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E"),
("302", "Ayşe", "Demir", datetime(2004, 4, 12), "K"),
("303", "Mehmet", "Kaya", datetime(2006, 7, 23), "E"),
("304", "Fatma", "Çelik", datetime(2003, 9, 8), "K"),
("305", "Ali", "Şahin", datetime(2005, 11, 2), "E")
]

# Student.saveStudents(ogrenciler)      