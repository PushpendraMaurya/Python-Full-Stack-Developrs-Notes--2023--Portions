import mysql.connector as db
from prettytable import PrettyTable

mydb = db.connect(host = "localhost",user = "dbuser",passwd = "Squ@d123",database = "BasicDB")

mycursor = mydb.cursor()


# mycursor.execute("select * from Info where address = Ambernath")
# mydata = mycursor.fetchone()
# for i in mydata:
#     print(i)


mycursor.execute("select * from Info")
mydata = mycursor.fetchall()
# for i in mydata:
#     print(i)

x = PrettyTable()
x.field_names("ID","NAME","ADDRESS","PHONE_NO","D-O-B","AGE")
for data in mydata:
    x.add_row(list(data))
print(x)
