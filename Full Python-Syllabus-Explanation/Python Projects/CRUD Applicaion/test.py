import mysql.connector as db

class CRUD:
    def __init__(self):

        #create database part ......
        mydb = db.connect(host = 'localhost',
        port = '3306',
        user = 'root',
        password = 'root')

        query = '''create database if not exists Students;'''

        cur = mydb.cursor()
        cur.execute(query)

        mydb.close()
        # print("data base created successfully")

         # create table in database.........
        
        mydb = db.connect(host = 'localhost',
        port = '3306',
        user = 'root',
        password = 'root',
        database = 'Students')

        query = ''' create table if not exists StudentsInfo(
                    s_id int primary key auto_increment ,
                    s_name varchar(50) not null,
                    s_salary bigint not null,
                    s_contact bigint not null ,
                    s_location varchar(50) not null);'''

        cur = mydb.cursor()
        cur.execute(query)
        mydb.close()
        # print("tabe has created")

        # create a function cause required call again an again ....
        
        def connection(self):
            self.mydb = db.connect(host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'StudentsInfo')

            self.cur = self.mydb.cursor()
        # print('finction done')

        def InsertData(self,name,salary,locatoion):
            pass
        def ReadData(self):
            pass
        def DeleteData(self,contact):
            pass
        def UpdateDate(self,unique,name,salary,contact,location):
            pass





App = CRUD()