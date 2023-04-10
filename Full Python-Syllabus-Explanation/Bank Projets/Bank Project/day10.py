import mysql.connector as db
import re
import time
import os

class Admin:
    #create database ...............
    def __init__(self):

        # this file is us eto make directory us ed for text file
        try:
            os.mkdir("All File")

        except:
            pass
     
        mydb = db.connect(host='localhost',user='root',port='3306',passwd='root')
        query = '''create database if not exists BasicDB;'''
        cur = mydb.cursor()
        cur.execute(query)
        mydb.close()


        #create table for admin...............
        self.connection()
        query = '''create table if not exists Admin_suraj(a_id int primary key unique , a_username varchar(50),a_password varchar(50));'''
        self.cur.execute(query)
        self.mydb.close()

    
        #Admin Default Data

        self.a_id = 1
        self.a_username = 'admin'
        self.a_password = 'admin'
        self.Add_AdminValue(self.a_id,self.a_username,self.a_password)
    
    #This is is used to connect Python to Mysql in BasicDB as database name
    def connection(self):
        self.mydb = db.connect(host='localhost',user='root',port='3306',passwd='root',database='BasicDB')
        self.cur = self.mydb.cursor()
       
    
    #This method is used to add default admin data ................
    def Add_AdminValue(self,a_id,a_username,a_password):
        self.connection()
        try:
            data = (a_id,a_username,a_password)
            query = '''insert into Admin_suraj(a_id,a_username,a_password) values (%s,%s,%s);'''
            self.cur.execute(query,data)
            self.cur.execute("commit;")
            self.mydb.close()

        except:
            pass

    def AdminLogIn(self,a_username,a_password):
        self.connection()
        data = (a_username,)
        query =''' select a_username,a_password from Admin_suraj where a_username = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    def checkpass(self,passwd):
        self.connection()
        data = (passwd,)
        query = '''select a_username, a_password from Admin_suraj where a_password = %s;'''
        self.cur.execute(query,data)
        record =self.cur.fetchone()
        self.mydb.close()
        return record

    def ChangeAdminUsername(self,n_username,passwd):
        self.connection()
        data  = (n_username,passwd)
        query =''' update Admin_suraj set a_username = %s where a_password = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "SuccessFully Admin username changed "


    def ChangeAdminPassword(self,n_password,passwd):
        self.connection()
        data  = (n_password,passwd)
        query =''' update Admin_suraj set a_password = %s where a_password = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "SuccessFully Admin Password changed "

    def RemoveAccount(self , email , acc_no):
        self.connection()
        data=(email , acc_no)
        query = '''delete from UserDetails_s where email = %s && account_no = %s;'''
        self.cur.execute(query , data)
        self.cur.execute("commit;")
        self.mydb.close()

        os.remove(f"All File/{email}.txt")

        return True

class Bank(Admin):
    def __init__(self):
        super().__init__()

        # create table UserDetails_s
        self.connection()
        query = '''
            create table if not exists UserDetails_s(cid int primary key auto_increment ,
            cname varchar(50) not null,
            contact varchar(20) not null unique , 
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
        account_no = 1000000

        self.connection()
        query = '''select account_no from UserDetails_s order by cid desc limit 1;'''
        self.cur.execute(query)
        record = self.cur.fetchone()
        # print(record)

        self.mydb.close()

        if record is not None:
            account_no = record[0]+1
            return account_no

        else:
            return account_no

    #this method is used to check contact & Email
    def CheckInfo(self , c_contact = None, c_email = None):
        self.connection()

        data = (c_contact , c_email)

        query = '''select contact , email from UserDetails_s where contact = %s or email = %s;'''

        self.cur.execute(query , data)
        
        record = self.cur.fetchone()

        # print(record)

        self.mydb.close()

        if record == None:
            return True

        elif record[0] == c_contact:
            return "Contact Already Exists"

        elif record[1] == c_email:
            return "\n**********Email Already Exists***********\n"

        



    #this method is used to create Account:
    def CreateAccount(self, c_name , c_contact , c_email , address  , created_at , account_no , amount ):

        self.connection()

        query = '''insert into UserDetails_s(cname , contact , email , address , created_at , account_no , amount , password) values (%s , %s , %s ,%s ,%s ,%s ,%s ,Null);'''

        data = (c_name , c_contact , c_email , address  , created_at , account_no , amount)

        self.cur.execute(query , data)
        self.cur.execute("commit;")

        self.mydb.close()

        return True

    def ChangePass(self , account_no , pass1):
        self.connection()

        query = '''update UserDetails_s set password = %s where account_no =%s;'''

        data = (pass1 , account_no)
        self.cur.execute(query , data)
        self.cur.execute("commit;")
        self.mydb.close()
    

    def CheckPassExist(self , account_no):
        self.connection()

        query = '''select password from UserDetails_s where account_no = %s;'''
        data = (account_no,)
        self.cur.execute(query , data)
        record = self.cur.fetchone()

        self.mydb.close()
        return record

    def UserLogin(self , email , pass1):
        self.connection()
        query = '''select email from UserDetails_s where email=%s && password=%s'''
        data=(email , pass1)
        self.cur.execute(query , data)
        record = self.cur.fetchone()

        self.mydb.close()
        return record
                        






class Regx(Bank):
    def __init__(self):
        super().__init__()


    def NameValidation(self,c_name):
        p = "^[a-zA-Z\ ]+$"
        if re.match(p,c_name):
            return True

        else:
            return False

    def ContactValidation(self,c_contact):
        p = "^[6-9]\d{9}"
        if re.match(p,c_contact):
            return True

        else:
            return False



    def EmailValidation(self,c_email):
        p = "^[a-zA-Z0-9\_\.]+@[a-z]+\.[a-z]+$"
        if re.match(p,c_email):
            return True

        else:
            return False




# application start with here...........

App = Regx()

while True:
    print("\n****** Bank Management System *******\n")
    print("1- Admin Login \n2- User Login \n3- Loan Section \n4 - Generate Password  \n5 - Exit \n")
    ch = input("Enter Your Choice :")

    #This is section used for Admin Task.........
    if ch =="1":
        print("\n************** Admin Login Section*****************\n")
        a_username = input("Enter Your Username :")
        a_password = input("Enter Your Password :")
        admin = App.AdminLogIn(a_username,a_password)
        if admin ==None:
            print("************** Invalid UserName *************")
        
        else:
            if a_password !=admin[1]:
                print("******* Invalid Password *******")

            else:
                print("\n****** SuccessFully Logged In **************\n")

                # admin Authentication
                while True:
                    print("************ Admin Section **************")
                    print("1- Add User \n2- Remove User \n3- Change Admin Password \n4 - Check User loan \n5 -Admin Logout \n")

                    ach = input("Enter Your Choice :")
                    
                    #add  user section..........
                    if ach =="1":
                        print("\n********* Create User Account Section ***************\n")
                        LoanStatus = False
                        # name Validation 
                        while True:
                            c_name = input("Enter Your Name :")
                            x = App.NameValidation(c_name)
                            if x == True:
                                break
                            else:
                                print("\n ************** Invalid Name **************** \n")

                        # contact Validation 
                        while True:
                            c_contact = input("Enter Your Contact :")
                            x = App.ContactValidation(c_contact)
                            if x == True:
                                break

                            else:
                                print("\n****************** Invalid Contact*******************\n")

                        
                         #Email Validation 
                        while True:
                            c_email = input("Enter Your Email :")
                            x = App.EmailValidation(c_email)
                            if x == True:
                                break

                            else:
                                print("\n****************** Invalid Email *******************\n")

                        #address field
                        address = input("Enter Address :")

                        #created_at field
                        created_at = time.strftime("%Y-%m-%d")

                        #account Number
                        account_no = App.CreateAccountNumber()
                        # print(account_no)

                        #amount
                        amount = 0

                        #password

                        check_info = App.CheckInfo(c_contact , c_email)

                        if check_info == True:

                            bank_account = App.CreateAccount(c_name , c_contact , c_email , address , created_at , account_no , amount)

                            if bank_account == True:

                                # cReate file to store user Info

                                with open(f"All File/{c_email}.txt" , "a") as file:
                                    file.write(f"User Name : {c_name}\n")
                                    file.write(f"User Contact Number : {c_contact}\n")
                                    file.write(f"User Email-ID : {c_email}\n")
                                    file.write(f"User Address : {address}\n")
                                    file.write(f"User Account Creation Date : {created_at}\n")
                                    file.write(f"User Account Number : {account_no}\n")


                                print("\n****************** Account Successfully Created ***********\n")

                        else:
                            print(f"**************** {check_info} ******************\n")

                            


                    #remove user section..............
                    elif ach =="2":
                        print("\n************** Close Account ***************\n")

                        while True:
                            email = input("Enter Email-ID to close your Account : ")
                            x=App.EmailValidation(email)
                            if x== True:
                                break
                            else:
                                print("\n********** Invalid Email-ID *************\n")

                        CheckUser = App.CheckInfo(c_email=email)
                        if CheckUser == True:
                            print("\n*********** User Does not exists *************\n")

                        else:
                            acc_no = input("Enter User Account Number : ")
                            r_acc = App.RemoveAccount(email , acc_no)

                            if r_acc == True:
                                print("\n********** Account Successfully Closed ************\n")
                            else:
                                print("\n*********** Incorrect Account Number *****************\n")

                    #change admin password............
                    elif ach =="3":
                        print("\n***************** Change Admin Username and Password **************\n")
                        print("1- Change Admin UserName \n2- Change Admin PassWord \n")
                        cch = input("Enter Your Choice to Change ")

                        if cch =="1":
                            passwd = input("Enter Admin Password :")
                            x = App.checkpass(passwd)

                            if x ==None:
                                print("\n********** Invalid Admin Password ***********\n")
                            else:
                                n_username = input("Enter Your new UserName :")
                                x1 = App.ChangeAdminUsername(n_username,passwd)
                                print(f"\n*********** {x1}*****************\n")

                        elif cch =="2":
                            passwd = input("Enter Admin Password :")
                            x = App.checkpass(passwd)

                            if x ==None:
                                print("\n********** Invalid Admin Password ***********\n")
                            else:
                                # print(x)
                                n_password = input("Enter Your new Password :")
                                x1 = App.ChangeAdminPassword(n_password,passwd)
                                print(f"\n*********** {x1}*****************\n")


                        else:
                            print("\n********* Invalid Change Choice ***********\n ")

                        
                        

                    #check user loan.............
                    elif ach =="4":
                        pass

                    #Admin Logout Section..........
                    elif ach =="5":
                        print("*********** Admin Logout ***********")
                        break
                    else:
                        print("******** Invalid Admin Choice **********")            


    # This is section used for User Task ................
    elif ch =="2":
        print("\n*********** User Login Section *************\n")
        while True:
            email = input("Enter Email-ID")
            x=App.EmailValidation(email)
            if x == True:
                break
            else:
                print("\n************* Invalid Email-ID **************\n")

        pass1 = input("Enter Password : ")
        y = App.UserLogin(email , pass1)
        if y == None:
            print("\n************ Incorrect Password ***********\n")

        else:
            print("\n************** Successfully Login ***************\n")

    #This is section used for Loan Section.......
    elif ch =="3":
        pass

    # This is section used for Generate Password.........
    elif ch =="4":
        print("\n ************* Generate User Password ************\n")
        while True:
            data = input("Enter Contact or Email :")
            
            contact = False
            email = False
            if data.isdigit():
                v_contact = App.ContactValidation(data)
                if v_contact is True:
                    contact = App.CheckInfo(c_contact = data)
                    break
                else:
                    print("\n****************** Invalid Contact Number ***********\n")

            else:
                v_email = App.EmailValidation(data)
                if v_email is True:
                    email = App.CheckInfo(c_email = data)
                    break

                else:
                    print("\n************** Invalid Email-ID ****************\n")

        if (contact is True) or (email is True):
                print("\n**************** Account Does Not Exists ***********\n")

        else:
            account_no = input("Enter Your Account Number :")
            checkexit = App.CheckPassExist(account_no)
            if checkexit[0] is None:
                pass1 = input("Enter Password :")
                pass2 = input("Enter Confirm Password :")

                if pass1 == pass2:
                    App.ChangePass(account_no , pass1)
                    print("\n************ Pasword Succesfully Updated *************\n")
                else:
                    print("\n*********** Password MisMatched **********\n")
            else:
                print("\n*************** Password Already Updated **********\n")




    #This is section used for  Exit the application .............
    elif ch =="5":
        print("************** Thank You *************")
        break
    else:
        print("************ invalid Option ************** ")
 