import mysql.connector as db

mydb = db.connect(host = "localhost",user = "dbuser",passwd = "Squ@d123")

if db:
    print("Connected..")