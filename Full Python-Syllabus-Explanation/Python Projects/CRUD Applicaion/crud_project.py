import mysql.connector as db
import time 
from prettytable import PrettyTable
class CRUD:   
    def __init__(self):
        # create database
        mydb = db.connect(host = 'localhost',
        port = '3306',
        user= 'root',
        password = 'root')

        #create query for databse
        query = '''create database if not exists BasicDB;'''
        
        #create cursor to communicate with database
        cur = mydb.cursor()
        cur.execute(query)
        
        #close mydb as database otherwise net query creation time error..
        mydb.close()


        #create table 
        mydb = db.connect(host = 'localhost', 
                          port ='3306',
                          user ='root',
                          password = 'root',
                          database = 'BasicDB')

        #create query for table .....
        query = '''create table if not exists EmployeeInfo(
                    eid int primary key auto_increment ,
                    e_name varchar(50) not null,
                    e_doj varchar(50) not null,
                    e_salary bigint not null,
                    e_designation varchar(50) not null,
                    e_contact varchar(50) unique );
        
                    '''
        cur = mydb.cursor()
        cur.execute(query)
        mydb.close()
    
    # creating functions.....
    def connection(self):
        self.mydb = db.connect(host = 'localhost',user ='root',password = 'root',database ='BasicDB')
        self.cur = self.mydb.cursor()

    
    #this is method is used to insert the value
    def InsertDetails(self,name,doj,esalary,edesignation,econtact):
        self.connection()
        try:
            query ='''insert into EmployeeInfo(e_name,e_doj,e_salary,e_designation,e_contact) values 
                    (%s,%s,%s,%s,%s);'''
        
            data = (name ,doj,esalary,edesignation,econtact)
            self.cur.execute(query,data)
            self.cur.execute('commit;')
            self.mydb.close()
            return True

        except:
            return False

    # Fetch all the records on tables

    def ReadAllData(self):
        self.connection()
        query ='''select * from EmployeeInfo;'''
        self.cur.execute(query)
        records = self.cur.fetchall()
        return records
    

    # delete the records on tables
    
    def DeleteRecord(self,contact):
        self.connection()
        query = '''delete from EmployeeInfo where e_contact = %s;'''
        data = (contact,)
        self.cur.execute(query, data)
        self.cur.execute("commit ;")
        self.mydb.close()
        return "Data SuccesFully Deleted"
    

    def UpdataData(self,unique,e_name,e_doj,e_salary,e_designation,e_contact):
        self.connection()
        query ='''update EmployeeInfo set e_name ='{}', e_doj ='{}', 
        e_salary ={}, e_designation '{}',
        e_contact{} where unique = {} where unique = %s;'''
        data = (e_name,e_doj,e_salary,e_designation,e_contact)
        self.cur.execute(query,data)
        self.cur.execute("commit ;")
        self.mydb.close()
        return "Data SuccesFully Updated "


        # query = '''update EmployeeInfo set column  where e_contact = %s;'''
        # query = '''UPDATE EmployeeInfo SET e_contact WHERE e_contact = %s;'''
        # data = (contact,)
        # self.cur.execute(query,data)
        # self.cur.execute("commit ;")
        # self.mydb.close()
        # return "Data SuccesFully Updated "
        

    



# create instace of class   
app = CRUD()
while True:
    print("*************** This is My CRUD Application  *********** ")
    print("1 - Insert Query \n2 - Read Query \n3 - Delete Query \n4 - Update Query \n5 - For Exit the Application")


    #take user input to perfor operations...

    ch = input("Enter Your Choice :")

    if ch == "1":
        print("\n************ Insert Information  **********\n")
        name = input("Enter EmployeeInfo Name :")
        doj = time.strftime("%Y -%m -%d")
        esalary = int(input("Enter Your Salary :"))
        edesignation = input("Enter Your Designation :")
        econtact = input("Enter Your Contact :")

        x = app.InsertDetails(name,doj,esalary,edesignation,econtact)
        if x == True:
            print("\n************ Data SuccesFully **********\n")
        else:
            print("\n************ Something Went Wrong  **********\n") 

    elif ch == "2":
        print("\n********This is Read Data Page ***********\n")
        records = app.ReadAllData()
        x = PrettyTable()
        x.field_names = ["Id","EmployeeInfo","DateJoin","Salary","Designation","Contact"]
        x.add_rows(records)
        print(x)

    elif ch == "3":
        print("*************** Delete the Data ***********")
        contact = int(input("Enter Your Contact Number  :"))
        dch = input("Are You sure want to delete the records :(y/n) :")
        if dch =="y" or dch =="yes" or dch =="Y" or dch == "YES":
            a = app.DeleteRecord(contact)
            print(f"\n**************{a}***************\n")
        else:
            print("\n************** Process has Been Cancel***************\n")

    elif ch == "4":
        print("\n******** Data Update Page ************\n")
        unique = input("Enter your Unique :")
        name = input("Enter Your New  Name :")
        doj = time.strftime("%Y -%m -%d")
        esalary = int(input("Enter Your  New Salary :"))
        edesignation = input("Enter Your  New Designation :")
        econtact = input("Enter Your  New Contact :")
        u = app.UpdataData(unique,name,doj,esalary,edesignation,econtact)
        print(u)


    elif ch == "5":
        print("********* ! Thank You ! ******")
        break
    else:
        print("Invalid Input plz once your check !!!! ")

