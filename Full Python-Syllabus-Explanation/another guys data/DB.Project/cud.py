import mysql.connector as db
from prettytable import PrettyTable

class CRUD:
    def __init__(self):
        #Step 1 :- Connect to the database
        mydb = db.connect(host = "localhost",user = "dbuser",passwd = "Squ@d123")

        #Step 2 :- Create Cursor
        mycursor = mydb.cursor()

        #Step 3 :- Create Database If Not Exists
        query = """create database if not exists BasicDB"""
        mycursor.execute(query)

        #Connect To The Database
        self.mydb = db.connect(host = "localhost",user = "dbuser",passwd = "Squ@d123",database = "BasicDB")

        #New Cursor
        self.mycursor = self.mydb.cursor()

        #Create Table
        query = """create table if not exists Myinfo(id int primary key auto_increment,
        name varchar(25),
        address varchar(200),
        age int,
        contact bigint unique)"""
        self.mycursor.execute(query)


    def adddetails(self,name,address,age,contact):
        data = (name,address,age,contact)
        query = """insert into Myinfo(name,address,age,contact) values(%s,%s,%s,%s)"""
        self.mycursor.execute(query,data)
        self.mydb.commit()

    def readdata(self):
        query = """select * from Myinfo"""
        self.mycursor.execute(query)
        records = self.mycursor.fetchall()
        return records


c=CRUD()


while True:
    print("1.Insert Value\n2.Read All Data\n3.Update Data\n4.Delete Data\n5.Search Data\n6.Exit")
    choice = input("Enter Your Choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        age = input("Enter Age: ")
        contact = input("Enter Contact No: ")
        c.adddetails(name,address,age,contact)
        

    elif choice == "2":
        data = c.readdata()
        x = PrettyTable()
        x.field_names = ["Id","Name","Location","Age","Contact"]
        for records in data:
            x.add_row(list(records))
        print(x)


    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        print("Changes had been made......")
        break

    
    else:
        print("Invalid Choice!!!")


