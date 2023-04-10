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
        
        #close mydb as database otherwise not query creation time error..
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

    def checkuser(self,contact):
        self.connection()
        data = (contact,)
        query = '''select * from EmployeeInfo where e_contact = %s;'''
        self.cur.execute(query,data)
        record=self.cur.fetchone
        self.mydb.close()
        return record               

    def UpdateInfo(self,query,data):
        self.connection()
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "successfully data Updates"
        
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
        print("\n************ Update Sections ****************\n")
        print("1 - Update Employee Name \n2- Update Employee Salary \n3 - Update Designation")

        uch = input("Enter Your Choice to Updates :")
        contact = input("Enter Your Unique identity to Confirmations :")

        #check users 
        chk = app.checkuser(contact)
        if uch == None:
            print("\n********Employee is not Exists******\n")
        
        else:
            if uch =="1":
                print("Your Old name is {chk[1]}")
                new_name = input("Enter Your New Name  :")
                query = '''update EmployeeInfo set e_name = %s where e_contact = %s;'''
                data = (new_name,contact)
                x = app.UpdateInfo(query,data)
                print(f"\n*********{x}********\n")
            
            elif uch =="2":
                print("Your old Salary is {chk[3]}")
                new_salary = input("Enter Your New Salary :")
                query = '''update EmployeeInfo set e_salary = %s where e_contact = %s;'''
                data = (new_salary,contact)
                x = app.UpdateInfo(query,data)
                print(f"\n************{x}***********\n")

            elif uch =="3":
                print("Your Old Designation{chk[4]}")
                new_designation = input("Enter Your New Designation :")
                query = '''update EmployeeInfo set e_designation = %s where e_designation = %s;'''
                data = (new_designation,contact)
                x = app.UpdateInfo(query,data)
                print(f"\n************{x}*************\n")

          
            else:
                print("\n*********** Invalid updates Choice *******************\n")

        



    elif ch == "5":
        print("********* ! Thank You ! ******")
        break
    else:
        print("Invalid Input plz once your check !!!! ")

