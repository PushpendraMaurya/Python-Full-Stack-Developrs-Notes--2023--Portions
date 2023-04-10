import pickle

from student import *


n = int(input("Enter number of students:  "))
with open("hello1.txt","wb") as f:
    name = input("\nEnter name: ")
    roll = input("Enter Age: ")
    address = input("Enter Address")
    stu1 = Student(name,roll,address)
    pickle.dump(stu1,f)
print("Pickling Done!!!!!!")

