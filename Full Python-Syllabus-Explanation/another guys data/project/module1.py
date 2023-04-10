class Student:
    def __init__(self,name,rollNo,marks1,marks2,passW):
        self.name = name
        self.rollNo = rollNo
        self.marks1 = marks1
        self.marks2 = marks2
        self.passW = passW

    @classmethod
    def acceptStudentDetails(cls,name,rollNo,marks1,marks2,passW):
        ob=cls(name,rollNo,marks1,marks2,passW)
        l.append(ob)

    def displaytable(self,l):
        print("No\tName\tRollNo\tMarks1\tMarks2\tPassword")
        for i in range(l.__len__()):
            print(f"{i+1}\t{l[i].name}\t{l[i].rollNo}\t{l[i].marks1}\t{l[i].marks2}\t{l[i].passW}")

    def display(self,l):
        print("Name: ",l[i].name)
        print("RollNo: ",l[i].rollNo)
        print("Marks1: ",l[i].marks1)
        print("Marks2: ",l[i].marks2)
        print("Password: ",l[i].passW)

    def search(self,roll):
        for i in range(l.__len__()):
            if(l[i].rollNo == roll):
                return i
        
    def delete(self,rn):
        j=obj.search(rn)
        del l[j]

    def update(self,rno,rno1):
        k=obj.search(rno)
        rno = rno1
        l[k].rollNo = rno1   

l=[]
obj=Student("","","","","")        