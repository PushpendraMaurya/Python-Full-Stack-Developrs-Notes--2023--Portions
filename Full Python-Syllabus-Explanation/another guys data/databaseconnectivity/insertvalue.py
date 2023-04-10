import mysql.connector as db

mydb = db.connect(host = "localhost",user = "dbuser",passwd = "Squ@d123",database = "BasicDB")

mycursor = mydb.cursor()


query = """insert into Info(Name,address,contact,DOB,Age) values (%s,%s,%s,%s,%s)"""

# data = ("Saurav","Ambernath",3265478945,"2004-05-04",18)

# mycursor.execute(query,data)

# mydb.commit()

data = [("Sarbajeet","Ambernath",1236548975,"2002-04-15",20),("Hiten","Kalyan",1597536548,"2002-07-12",21)]
mycursor.executemany(query,data)
mydb.commit()

query = """select * from Info"""
mycursor.execute(query)
for mydata in mycursor:
    print(mydata)
