import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    user="root",
    password="root123",
    database="student"
)
mycursor=mydb.cursor()

mycursor.execute(
   """CREATE table EMAIL_DATA(
       id varchar(255),
       first_name varchar(255),
       last_name varchar(255),
       age varchar(255),
       gender  varchar(255),
       Gmail varchar(255),
       city varchar(255))""")

class StudRecorde():
  def execute(self):
    mycursor.execute("select * from EMAIL_DATA")
    mycursor.fetchall()
    variable=("INSERT INTO EMAIL_DATA(id,first_name,last_name,age,gender,Gmail,city) VALUES(%s,%s,%s,%s,%s,%s,%s) ")
    data=[(101,'Abhi' ,'Desai',19,'Male','adhidesai2004@gmail.com','Kolhapur'),
      (102,'Amit','Varote',20,'Male','amit02varote@gemail.com','Kolhapur'),
      (103,'Blaram','Desai',19,'Male','blaram200504@gmail.com','kagal'),
      (104,'Harshita','kamt',20,'Female','harshitakamt@gmail.in','Mumbai'),
      (105,'Hari','Hebale',19,'Male','harihebale56@gmaol.com','Mumbai'),
      (106,'Gouri','Patil',20,'Female','gouripatil34@gmil.com','Kolhapur'),
      (107,'Akshata','Patil',19,'Female','akakshatapatil20@gmail.com','Ahmedabad'),
      (108,'Bharat','Chaugule',26,'Male','bharatchaugule78@gmail.com','Pune'),
      (109,'Diva','Rote',24,'Female','diva2344rote@gmail.com','Kanpur'),
      (110,'Gayatri','Domane',24,'Female','gayatridomane2323@gamil.com','Nashik'),
      (111,'Mahavir','Rauta',25,'Male','mahavirrauta234@gmail.com','Mumbai'),
      (112,'Kirsh','Bhoja',24,'Male','krishbhoja89@gmail.com','Kanpur'),
      (113,'Smruti','Bisht',26,'Male','smrutibisht45@gmail.com','Haldvani'),
      (114,'Gourav','Bisht',23,'Male','gouravbisht45@gmail.com','Mumbai'),
      (115,'Gouri','Rote',24,'Female','sgourirote2200@gmail.com','Mumbai'),
      (116,'Ramesh','lyer',26,'Male','rameshlyer35@gmail.com','Chennai'),
      (117,'Aman','Jain',25,'Male','aman34jain@gmail.con','jaipur'),
      (118,'Rashmika','Sawant',23,'Female','rashmikaoffical@gmail.com','Mumbai'),
      (119,'Ritika','lyer',19,'Female','ritikalyer@gmail.com','Chennai'),
      (120,'Rohini','Mathura',25,'Female','mathurarohini@gmai.com','Kanpur')
      ]
    for i in data:
       mycursor.execute(variable,i)
       mydb.commit()
    
  def All_data(self):
      mycursor.execute("select * from EMAIL_DATA;")
      myresult=mycursor.fetchall()
      print("\n\t ALL inserted DATA")
      for i in myresult: print(i) 

  def create_table_correct(self):
    mycursor.execute("""create table correct_data like EMAIL_DATA""")
    myresult=mycursor.fetchall()
    for i in myresult: print(i) 

  def insert_table_correct(self):     
    mycursor.execute("""insert into  correct_data 
                       select * from EMAIL_DATA 
                       where  Gmail like '%@gmail.com%';""")
    print("\n\t Correct Data\n")
    mycursor.execute("select * from correct_data;")
    myresult=mycursor.fetchall()
    for i in myresult: print(i) 

  def create_table_wrong(self):
     mycursor.execute("""create table wrong_data like EMAIL_DATA""")
     myresult=mycursor.fetchall()
     for i in myresult: print(i) 

  def insert_table_wrong(self): 
       mycursor.execute("""insert into  wrong_data 
                       select * from EMAIL_DATA """)
       print("\n\tWrong Data\n")
       mycursor.execute("""select * from wrong_data where id Not IN(select id from correct_data )  """  )
       myresult=mycursor.fetchall()
       for i in myresult: print(i) 
  
obj=StudRecorde()
obj.execute()
print("\t------Student Records-------")
print("\t1) ALL inserted Gmail DATA\n\t2)Correct Gmail Data AND Wrong Gmail Data ")
try: option=int(input("\n\t Choose your option from above:"))
except IndexError: print("\nenter correct option")

if (option==1):obj.All_data()
elif(option==2):
  obj.create_table_correct()
  obj.insert_table_correct()
  obj.create_table_wrong()
  obj.insert_table_wrong()
