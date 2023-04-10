import mysql.connector as db

mydb = db.connect(host = 'localhost',port = '3306',user='dbuser' ,passwd = 'Squ@d123')
print("its a conncted")