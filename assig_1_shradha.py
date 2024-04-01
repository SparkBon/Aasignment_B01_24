import mysql.connector

mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="Shradha@123"
    ) 

mycursor=mydb.cursor()

class data_base:
     def __init__(self, Fr_om, T_o):
        self._Fr_om =Fr_om
        self._T_o =T_o

     def create_db(self):
          mycursor.execute(f"Create database Assign_db ")

     def create_table(self):
          mycursor.execute("""CREATE TABLE DATA_TBL 
                        (Id int,
                        First_Name varchar(255),
                        Last_Name varchar(255),
                        Email varchar(255),
                        Salary bigint,
                        Gender varchar(20),
                        Age int,
                        City varchar(50))
                        """)     


print("Enter salary range below ")
fr_om = int(input("FROM:  "))
t_o = int(input("TO:  "))
obj = data_base(fr_om, t_o) 
 
obj.create_db()

mycursor.execute("use Assign_db") 

obj.create_table()

