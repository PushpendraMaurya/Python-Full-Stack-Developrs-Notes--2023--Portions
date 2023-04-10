import mysql.connector as db

mydb = db.connect(host = "localhost",user = "dbuser",passwd = "Squ@d123",database = "BasicDB")

mycursor = mydb.cursor()

mycursor.execute(""" create table if not exists Info(Id int primary key auto_increment,Name varchar(20),
address varchar(200),
contact bigint,
DOB date,
Age int) """)

mycursor.execute("show tables")

for table in mycursor:
    print(table)