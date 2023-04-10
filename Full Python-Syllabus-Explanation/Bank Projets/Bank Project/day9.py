import mysql.connector as db
import re
import time

class Admin:
    def __init__(self):
        # create database
        mydb = db.connect(host = "localhost" , user = "dbuser" , passwd = "Squ@d123")
        query = '''create database if not exists BasicDB; '''
        cur = mydb.cursor()
        cur.execute(query)
        mydb.close()
        
        # create table for Admin
        self.connection()
        query = '''create table  if not exists Admin_Rupa(a_id int primary key , 
        a_username varchar(100),
        a_password varchar(100));'''
        self.cur.execute(query)
        self.mydb.close()
        
        
        #Admin Default data
        self.a_id = 1
        self.a_username = "admin"
        self.a_password = "admin"
        self.AddAdminValue(self.a_id,self.a_username,self.a_password)
    
    #this method used to python to mysql BasicDB database
    def connection(self):
        
        self.mydb=db.connect(host = "localhost" , user = "dbuser" , passwd = "Squ@d123" ,database = "BasicDB")
        self.cur=self.mydb.cursor()
        
    #This method used to add admin default data
    def AddAdminValue(self,a_id,a_username,a_password):
        self.connection()
        try:
            
            data = (a_id,a_username,a_password)
            query = '''insert into Admin_Rupa(a_id,a_username,a_password) values(%s,%s,%s);'''
            self.cur.execute(query,data)
            self.cur.execute("commit;")
            self.mydb.close() 
             
        except:
            pass        
        
        
    # This method used to admin login
    def AdminLogin(self,a_username , a_password):
        # get admin data from databases
        self.connection()
        data = (a_username,)
        query = '''select a_username,a_password from Admin_Rupa where a_username = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        
        return record
    
    
    def checkpass(self,passwd):
        self.connection()
        data = (passwd ,)
        query = '''select a_username,a_password from Admin_Rupa where a_password = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record
    
    
    def ChangeAdminUsername(self,passwd,n_username):
        self.connection()
        data = (n_username,passwd)
        query = '''update Admin_Rupa set a_username = %s where a_password = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        
        return "Successfully Admin Username Changed"
    
    def ChangeAdminPassword(self,n_password,oldpass):
        self.connection()
        data = (n_password,oldpass)
        query = '''update Admin_Rupa set  a_password = %s where a_password = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "Successfully Admin Password Changed"
              
        
class Bank(Admin):
    def __init__(self):
        super().__init__()
        
        #create table UserDetails_j
        
        self.connection()
        query = '''
            create table if not exists UserDetails_j(c_id int primary key auto_increment,
            c_name varchar(50) not null,
            contact varchar(20) not null unique,
            email varchar(100) not null unique,
            address text not null,
            created_at date not null,
            account_no bigint not null unique,
            amount bigint not null,
            password varchar(100));
            '''
        
        self.cur.execute(query)
        self.mydb.close()
        
    def CreateAccountNumber(self):
        account_no = 10000000
        
        self.connection()
        query = ''' select account_no from UserDetails_j order by c_id desc limit 1;'''
        self.cur.execute(query)
        record = self.cur.fetchone()
        #print (record)
        
        self.mydb.close()
        
        if record is not None:
            account_no = record[0]+1
            return account_no
        else:
            return account_no
        
        
    def CheckInfo(self,c_contact = None,c_email = None):
        
        self.connection()
        data = (c_contact,c_email)
        
        query = '''select contact,email from UserDetails_j where contact = %s or email = %s;'''
        
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        # print(record)
        
        
        self.mydb.close()
        
        if record is None:
            return True
        elif record[0] == c_contact:
            return "Contact Exists"
        elif record[1] == c_email:
            return "Email Exists"
        
        
        
    
    def CreateAccount(self,c_name , c_contact , c_email , address , created_at , account_no , amount):
        self.connection()
        query = '''insert into UserDetails_j(c_name ,contact,email,address,created_at,account_no,amount,password) values(%s,%s,%s,%s,%s,%s,%s,Null); '''
        
        data = (c_name , c_contact , c_email , address , created_at , account_no , amount)
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        
        return True
    
    def ChangePass(self,pass1,account_no):
        self.connection()
        query ='''update UserDetails_j set password = %s where account_no = %s;'''
        
        data = (pass1,account_no)
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        
    def checkpassexists(self,account_no):
        self.connection()
        query = '''select password from UserDetails_j where account_no=%s;'''
        data = (account_no, )
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record
        
        
class RegEx(Bank):
    def __init__(self):
        super().__init__()
    def NameValidation(self,c_name):
        ptr=r"^[a-zA-Z\ ]+$"
        if re.match(ptr,c_name):
            return True
        else:
            return False
        
    def ContactValidation(self,c_contact):
        ptr=r"^[6789]\d{9}$"
        if re.match(ptr,c_contact):
            return True
        else:
            return False
        
    def EmailValidation(self,c_email):
        ptr=r"^\b[a-zA-Z0-9\.\_]+@[a-z]+\.[a-z]+\b"
        if re.findall(ptr,c_email):
            return True
        else:
            return False        
    
#Apllication start from here

app = RegEx()
while True:
    print("\n************* Bank Management System ************\n")
    print("\n1 - Admin login \n2 - User login \n3 - Loan section \n4 - Genrate user password \n5 - Exit \n")
    ch =input("Enter your choice :")
    
    #This section use for Admin task
    
    if ch == "1":
        print("\n************ Admin Login Section *************\n")
        a_username = input("Enter admin Username:")
        a_password = input("Enter Admin Passwprd:")
        
        admin = app.AdminLogin(a_username, a_password)
        if admin == None:
            print("\n************ Invalid Admin Username ***************\n")
            
        else:
            if a_password != admin[1]:
                print("\n************** Invalid Admin Password **************\n")
                
            else:
                print("\n************ suceessfully Logged In ***************\n")
                
                #admin authenticated
                while True:
                    print("\n************* Admin Section *************\n")
                    print("1 - Add User \n2 - Remove User \n3 - Change Admin Password \n4 - Check User Loan \n5 - Admin Logout \n")
                    
                    ach = input("Enter admin Choice :")
                    
                    #add user section
                    if ach == '1':
                        print("\n********* Create Account Section **********\n")
                        LoanStatus=False
                        #Name validation
                        while True:
                            c_name=input("Enter Customer Name :")
                            x=app.NameValidation(c_name)
                            if x==True:
                                break
                            else:
                                print("\n****** Invalid Name Input ***********\n")
                                
                        #contact validation
                        while True:
                            c_contact=input("Enter Contact Number :")
                            x1=app.ContactValidation(c_contact)
                            if x1==True:
                                break
                            else:
                                print("\n********* Invalid Contact ********\n")
                                
                                
                        #email validation
                        while True:
                            c_email=input("Enter your EmailId :")
                            x2=app.EmailValidation(c_email)
                            if x2==True:
                                break
                            else:
                                print("\n*********** wrong Emailid *********\n")
                                
                        #address
                        address=input("Enter your Address :")
                        
                        #account creation date
                        created_at=time.strftime("%Y-%m-%d")
                        
                        #account_no create
                        account_no=app.CreateAccountNumber()
                        print(account_no)
                        
                        #amount created
                        amount = 0
                        
                        #password
                        check_info = app.CheckInfo(c_contact,c_email)
                        
                        if check_info is True:
                            bank_account = app.CreateAccount(c_name , c_contact , c_email , address , created_at , account_no , amount)
                            
                            if bank_account == True:
                                print("\n************ Account Sucessfully Created *************\n")
                        else:
                            print(f"********** {check_info} *************\n")
                    
                                
                        
                    
                    
                    #remove user section
                    elif ach == '2':
                        pass
                    
                    #change admin password section
                    elif ach == '3':
                        print("\n*********** Change Admin Username and Password ************\n")
                        print("1 - Change Admin Username \n2 - Change Admin Password \n")
                        cch = input("Enter Your Choice to Change :")
                        
                        if cch == '1':
                            passwd = input("Enter Admin Password :")
                            x= app.checkpass(passwd)
                            
                            if x == None:
                                print("\n************ Invalid Admin Password **********\n")
                                
                            else:
                                n_username = input("Enter your Username :")
                                
                                x1 = app.ChangeAdminUsername(passwd,n_username)
                                print(f"\n********** {x1} **********\n")
                                
                        elif cch == "2":
                            oldpass = input("Enter old password :")
                            y = app.checkpass(oldpass)
                            
                            if y == None:
                                print("\n********** invalid old password *************\n")
                            else:
                                n_password = input("Enter your New password :")
                                y1 = app.ChangeAdminPassword(n_password,oldpass)
                                print(f"\n********* {y1} **********\n")
                                
                                
                        else:
                            ("\n********** Invalid Password ***********\n")
           
                        
                    
                    #check user loan section
                    elif ach == '4':
                        pass
                    
                    elif ach == '5':
                        print("\n************ Admin Logout *************\n")
                        break
                    
                    else:
                        print("\n*********** Invalid Admin Choice ************\n")
                
            
                    
                
    
    
    # this section used  for User task
    
    elif ch == "2":
        pass
    
    # This section used for loan task
    elif ch == "3":
        pass
    
    #This section used for Genrate user
    elif ch == "4":
        print("\n************ Generate User Password ***************\n")
        
        while True:
            data = input("Enter Contact or Email :")
            
            contact = False
            email = False
            if data.isdigit():
                
                v_contact = app.ContactValidation(data)
                if v_contact is True:
                    contact = app.CheckInfo(c_contact = data)
                    break
                else:
                    print("\n************ Invalid Contact Number ***********\n")
                    
            else:
                v_email = app.EmailValidation(data)
                if v_email is True:
                    email = app.CheckInfo(c_email = data)
                    break
                
                else:
                    print("\n************* Invalid Email - ID ************\n")
                    
        if (contact is True) or (email is True):
            print("\n********** Account Does Not Exists *************\n")
                
            
        else:
            account_no = input("Enter Your Account Number :")
            checkexist=app.checkpassexists(account_no)
            if checkexist[0] is None:
            
                pass1 = input("Enter Password :")
                pass2 = input("Enter Confirm Password :")
                
                if pass1 == pass2:
                    app.ChangePass(pass1,account_no)
                    print("\n********* Password Successfully Updated ***********\n")
                else:
                    print("\n********** Password Mismatch ************\n")
            else:
                print("\n********** Password already update ***********\n")
                
        
        
    
    elif ch == "5":
        print("\n*********** Thank You *************\n")
        break
        
    
    else:
        print("\n*********** Invalid choice ***************\n")    
  