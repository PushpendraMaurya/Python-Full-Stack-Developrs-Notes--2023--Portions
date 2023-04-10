import mysql.connector as db

mydb = db.connect(host = "localhost",user = "dbuser",passwd = "Squ@d123")

mycursor = mydb.cursor()

# mycursor.execute("create database if not exists saurav")

mycursor.execute("show databases")

for database in mycursor:
    print(database)
