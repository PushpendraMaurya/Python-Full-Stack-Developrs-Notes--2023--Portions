import mysql.connector as db
import re
import time
class Admin:
    #create database ...............
    def __init__(self):
     
        mydb = db.connect(host='localhost',user='root',port='3306',passwd='root')
        query = '''create database if not exists BasicDB;'''
        cur = mydb.cursor()
        cur.execute(query)
        mydb.close()


        #create table for admin...............
        self.connection()
        query = '''create table if not exists Admin_Pushpendra(a_id int primary key unique , a_username varchar(50),a_password varchar(50));'''
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
            query = '''insert into Admin_Pushpendra(a_id,a_username,a_password) values (%s,%s,%s);'''
            self.cur.execute(query,data)
            self.cur.execute("commit;")
            self.mydb.close()

        except:pass

    def AdminLogIn(self,a_username,a_password):
        self.connection()
        data = (a_username,)
        query =''' select a_username,a_password from Admin_Pushpendra where a_username = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    def checkpass(self,passwd):
        self.connection()
        data = (passwd,)
        query = '''select a_username, a_password from Admin_Pushpendra where a_password = %s;'''
        self.cur.execute(query,data)
        record =self.cur.fetchone()
        self.mydb.close()
        return record

    def ChangeAdminUsername(self,n_username,passwd):
        self.connection()
        data  = (n_username,passwd)
        query =''' update Admin_Pushpendra set a_username = %s where a_password = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "SuccessFully Admin username changed "


    def ChangeAdminPassword(self,n_password,passwd):
        self.connection()
        data  = (n_password,passwd)
        query =''' update Admin_Pushpendra set a_password = %s where a_password = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "SuccessFully Admin Password changed "



class Bank(Admin):
    def __init__(self):
        super().__init__()

        # create table UsereDetails_j

        self.connection()
        query = '''
            create table if not exists UserDetails_j(cid int primary key auto_increment,
            cname varchar(50) not null,
            contact varchar(20) not null ,
            email varchar(100) not null unique ,
            address text not null,
            created_at date not null,
            account_no bigint not null unique,
            amount bigint not null,
            password varchar(100) );
        '''
        self.cur.execute(query)
        self.mydb.close()


    def CreateAccountNumber(self):
        acount_no = 10000000

        self.connection()
        query = '''select  account_no from UserDetails_j order by cid desc limit 1;'''
        self.cur.execute(query)
        record = self.cur.fetchone()
        # print(record)

        self.mydb.close()

        if record is not None:
            acount_no = record[0]+1
            return acount_no
        else:
            return acount_no
        




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
        # p =("(0|91)?[-\ s]?[6-9][0-9]{9}")

        p = "^([6-9][0-9]{9})+$"
        if re.match(p,c_contact):
            
            return True

        else:
            
            return False



    def emailValidation(self,c_email):
        # p = ("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w[.]\w{2,3}$")
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
            print("** Invalid UserName *************")
        
        else:
            if a_password !=admin[1]:
                print("******* Invalid Password *******")

            else:
                print("**** SuccessFully Logged In **************")

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
                                print("\n****************** Invalid Contact *******************\n")

                        
                         #Email Validation 
                        while True:
                            c_email = input("Enter Your Email :")
                            x = App.emailValidation(c_email)
                            if x == True:
                                break

                            else:
                                print("\n****************** Invalid Email *******************\n")

                        # address field 
                        address = input("Enter Adress :")

                        # created_at field
                        created_at = time.strftime("%Y-%m-%d")

                        # account number 
                        
                        account_no = App.CreateAccountNumber()
                        print(account_no)


                        

                    #remove user section..............
                    elif ach =="2":
                        pass

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
        pass

    #This is section used for Loan Section.......
    elif ch =="3":
        pass

    # This is section used for Generate Password.........
    elif ch =="4":
        pass


    #This is section used for  Exit the application .............
    elif ch =="5":
        print("************** Thank You *************")
        break
    else:
        print("************ invalid Option ************** ")