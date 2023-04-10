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

        except:pass


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
        print("********* This Is Admin Login Section ********************")
        print("1- Admin logiIn \n2- User Login \n3- Loan Section \n4 - Generate Password \n5- Exit \n")
        ch = input("Enter Your Choice :")
        #This is Section used for Admin Task.........
        if ch == "1":
            print("********* Admin Login Section ******************")
            a_username = input("Enter Your UserName :")
            a_password = input("Enter Your PassWord :")

            admin = app.AdminLogin(a_username, a_password)
            if admin == None:                                    
                print("\n******* Invalid UserName ************\n")

            else:
                if a_password != admin[1]:
                    print("********* Invalid Password ****************")
                
                else:
                    print("\n******** SuccessFully Admin Logged In ***************\n")


                    # Admin Authenticated .....................


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
 