import mysql.connector as db
from prettytable import PrettyTable


mydb = db.connect(host = "localhost",user = "dbuser",password = "Squ@d123",database = "BasicDB")

mycursor = mydb.cursor()


query = "update Info set address = 'Ambernath' where id = 3"
mycursor.execute(query)
mydb.commit()


mycursor.execute("select * from Info")
mydata = mycursor.fetchall()
# for data in mydata:
#     print(data)

x = PrettyTable()
x.field_names = ["ID","NAME","ADDRESS","PHONE_NO","D-OB","AGE"]
for data in mydata:
    x.add_row(list(data))
print(x)

