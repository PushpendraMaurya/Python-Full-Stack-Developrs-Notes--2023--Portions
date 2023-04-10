import mysql.connector as db
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

        except:
            pass


    # this method is used to admin login
    def AdminLogin(self , a_username , a_password):
        # get admin data from database 
        self.connection()

        data = (a_username,)
        query  = '''select a_username,a_password from Admin_Pushpendra where a_username = %s;'''
        self.cur.execute(query , data)
        record = self.cur.fetchone()
        self.mydb.close()

        return record

    def chekpass(self , passwd):
        self.connection()

        data = (passwd,)
        query = '''select a_username , a_password from Admin_Pushpendra where a_password = %s ;'''

        self.cur.execute(query ,data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    def ChangeAdminUsername(self ,passwd , n_username):
        self.connection()

        data = (n_username,passwd )
        query = '''update Admin_Pushpendra set a_username = %s where a_password = %s;'''
        self.cur.execute(query , data)
        self.cur.execute('commit;')
        self.mydb.close()

        return "Successfully Admin Username Changed"

class Bank(Admin):
    def __init__(self):
        super().__init__()

class Regx(Bank):
    def __init__(self):
        super().__init__()


# application start with here...........

app = Regx()

while True:
    print("\n****** Bank Management System *******\n")
    print("1- Admin Login \n2- User Login \n3- Loan Section \n4 - Generate Password  \n5 - Exit \n")
    ch = input("Enter Your Choice :")

    #This is section used for Admin Task.........
    if ch =="1":
        print("\n************* Admin Login Section *********************\n")
        a_username = input("Enter Admin Username :")
        a_password = input("Enter Admin Password :")

        admin = app.AdminLogin(a_username , a_password)
        if admin == None:
            print("\n****************** Invalid Admin Username *************\n")
        
        else:
            if a_password != admin[1]:
                print("\n*************** Invalid Admin Password ***************\n")
            else:
                print("\n*************** Successfully Admin Logged In ******************\n")
                # admin authenticated 
                while True:
                    print("\n************* Admin Section **************\n")
                    print('1 - Add User \n2 - Remove User\n3 - Change Admin Password \n4 - Check User Loan \n5 - Admin Logout\n')

                    ach = input("Enter Admin Choice :")

                    # add user section 
                    if ach == '1':
                        pass

                    # remove user section
                    elif ach == '2':
                        pass

                    # change admin pass 
                    elif ach == '3':
                        print("\n********* Change Admin Username and Password **********\n")
                        print("1 - Change Admin Username \n2 - Change Admin Password \n")
                        cch = input("Enter Your Choice to Change :")

                        if cch == "1":
                            passwd = input("Enter Admin Password :")
                            x = app.chekpass(passwd)
                            
                            if x == None:
                                print("\n********* Invalid Admin Password *********\n")

                            else:
                                n_username = input("Enter Your New Username :")

                                x1 = app.ChangeAdminUsername(passwd , n_username)
                                print(f"\n************** {x1} *****************\n")




                        elif cch == "2":
                            pass

                        else:
                            print("\n************ Invalid Change Choice *********\n")


                    # loan section
                    elif ach == '4':
                        pass

                    elif ach == '5':
                        print("\n********** Admin LogedOut ************\n")
                        break

                    else:
                        print("\n*********** Invalid Admin Choice **********\n")



    

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
 