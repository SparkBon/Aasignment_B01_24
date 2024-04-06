import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivani"
)
mycursor=mydb.cursor()

def create_databases():
    mycursor.execute("create database std_data")
    mycursor.execute("Show Database")
    for i in mycursor:
        print(i)

def create_table():
    mycursor.execute(""" CREATE TABLE std_data
                            (Sr_N int,id varchar(255),firstN varchar(255),
                              lastN varchar(255),
                             age int,
                             gender varchar(255),
                             city varchar(255))""") 

def insert_record(): 
    var="insert into std_data(Sr_N,id, firstN,lastN, age,gender,city) VALUES(%s, %s, %s, %s,%s,%s,%s)"
    val=[
            (1,"Schandekar","Shivani","Chandekar",23,"Female","Kolhapur"),        
            (2,"Sgilbile","Shrddha","Gilbile",23,"Female","Aajara"),
            (3,"Pchimane","Pooja","Chimane",23,"Female","Chandgad"),
            (4,"Pkamble","Pranali","Kamble",23,"Female","Kagal"),
            (5,"Rpatil","Ravina","Patil",24,"Female","Belgavi"),  
            (6,"Asutar","Amruta","Sutar",23,"Female","Aajara"), 
            (7,"Anulkar","Aarti","Nulkar",23,"Female","Chandagd"),
            (8,"Jjadhav","Jyoti","Jadhav",23,"Female","Gadhinglaj"),
            (9,"Pdhabhole","Pratiksha","Dabhole",23,"Female","Gargoti"),
            (10,"Ngoral","Nilesh","Goral",23,"Male","Mumbai"),
            (11,"Njadhav","Nitesh","Jadhav",23,"Male","Pune"),
            (12,"Spatil","Sagar","Patil",23,"Male","Kolhapur"),  
            (13,"Obamne","Omkar","Bamane",23,"Male","Chandgad"), 
            (14,"Schandeakr","Sudeep","Chandeakr",24,"Male","Pune"),
            (15,"Spatil","Sandeep","Patil",24,"Male","Belgavi"),
            (16,"Smangle","Shubham","Mangle",24,"Male","Mumbai"),
            (17,"Spatil","Snehal","Patil",23,"Female","Belgavi"),
            (18,"Pdethe","Pooja","Dethe",24,"Female","Pandhrpur"),
            (19,"Rkasbe","Rupali","Kasbe",23,"Female","Solapur"),
            (20,"Rmore","Rutuja","More",22,"Female","Pune")
            
    ]
    city=[]
    user=input("Enter Your City Name:")
    for i in val:
        if user==i[6]:
            city.append(i)
            
    for x in city:
        mycursor.execute(var,x)
        mydb.commit()
        print(mycursor.rowcount,"record inserted.")

        
def fetch_record():

        mycursor.execute("select * from std_data")

        result= mycursor.fetchall()

        for i in result:
            print(i) 


create_databases()
mycursor.execute("use std_data")
create_table()
insert_record()
fetch_record()