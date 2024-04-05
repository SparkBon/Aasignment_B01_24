import mysql.connector

mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="Shradha@123",
     database="Assign_db"
    ) 

mycursor=mydb.cursor()

class data_base:
      def __init__(self, Fr_om, T_o):
        self._Fr_om =Fr_om
        self._T_o =T_o

      # def create_db(self):
      #    mycursor.execute(f"Create database Assign_db ")

      def create_table(self):
         
         try:
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
              
         except Exception as e:
            print("The error is : ", e)    


      def insert_data(self):

         IP="INSERT INTO DATA_TBL  (Id, First_Name, Last_Name, Email, Salary, Gender, Age, City) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
         V=[
                  (1001, "Shradha", "Gilbile", "shradha@gmail.com", 80000, "female", 22, "Mumbai"),
                  (1002, "Ditya", "patel", "ditya@gmail.com",45000, "female", 22," Pune" ),
                  (1003, "Ram", "patil", "ram@gmail.com", 70000, "male", 25, "Mumbai "),
                  (1004, "Raj", "Jadhav", "raj@gmail.com", 55000, "male", 23, "Kolhapur" ),
                  (1005, "Yash", "Shinde", "Shinde@gmail.com", 60000, "male", 26, "Nashik" ),
                  (1006, "Tanmay", "Pandit", "tanmay@gmail.com", 54000, "male", 25, "pune" ),
                  (1007, "Aadya", "Mehta", "aadya@gmail.com", 60000, "female", 22, "MUmbai" ),
                  (1008, "vaishnavi", "Pandit", "vaishnavi@gmail.com", 60000, "female", 23,"Mumbai" ),
                  (1009, "Aaradhya", "mohite", "aaradhya@gmail.com", 45000, "female", 24,"Kolhapur "),
                  (1010, "Pratik", "Mohite", "pratik@gmail.com", 55000, "male", 22, "pune"),
                  (1011, "Amol", "Gilbile", "amol@gmail.com", 65000, "male", 20, "Mumbai"),
                  (1012, "Trupti", "Gilbile", "trupti@gmail.com", 80000, "female", 24,"Mumbai"),
                  (1013, "Viraj", "Pant", "viraj@gmail.com", 35000, "male", 21,"Sangli"),
                  (1014, "Rupak", "Jadhav", "rupak@gmail.com", 40000, "male",22 , "Delhi" ),
                  (1015, "Siddesh", "Desai", "siddesh@gmail.com", 50000, "male", 26, "Kolhapur"),
                  (1016, "Ira", "Gupta", "ira@gmail.com", 40000, "female", 23, "Gujrat"),
                  (1017, "Neha", "Joshi", "Neha@gmail.com", 54000, "female", 25, "Pune"),
                  (1018, "Vaibhav", "Patil", "vaibhav@gmail.com", 50000, "male", 22, "Mumbai"),
                  (1019, "Nitya", "Mangle", "nitya@gmail.com", 45000, "female", 23, "Kolhapur" ),
                  (1020, "Aarav", "Mohite", "aarav@gmail.com", 50000, "male", 25,"Pune" )
                  ]
         
         for i in range(1): 
            try:      
               if self._Fr_om and self._T_o in range(30000, 80001):

                  Salary=[ records for records in V if records[4] in range(self._Fr_om, self._T_o + 1 )]
                  
                  #  Salary=[]

                  #  for i in V:
                  #      if i[4] in range(self._Fr_om, self._T_o + 1): 
                  #         Salary.append(i)  


               for i in Salary:    
                  mycursor.execute(IP, i)
                  mydb.commit()
                  print(mycursor.rowcount,"record inserted")
               obj.select()   

            except:
               print("There is no one between these pay ranges. Enter the range from 30000 to 80000")
               break     


      def select(self):
         try:

            mycursor.execute(f"""select * from data_tbl 
                             where Salary between {self._Fr_om} and {self._T_o}""")  
            
            myresult=mycursor.fetchall()
            for i in myresult:
               print(i) 

         except Exception as e:
            print("The error is : ", e)              



print("Enter salary range below ")
fr_om = int(input("FROM:  "))
t_o = int(input("TO:  "))

obj = data_base(fr_om, t_o) 
# obj.create_db()
mycursor.execute("use Assign_db") 
# obj.create_table()
obj.insert_data()


