from module1 import Student,l,obj
obj.acceptStudentDetails("a",1,2,3,4)
obj.acceptStudentDetails("b",2,2,3,4)
obj.acceptStudentDetails("c",3,2,3,4)

while True:
    
    print("\n1.Teachers login\n2.Students login\n3.Exit")
    ch=input("Enter Choice:-")
    if ch =="3":
        print("Exit")
        break
    
    while True:

        if ch =="1":            
            usert = "Teacher"
            passwt = "123"
            tUserid=input("Enter Userid: ")
            if tUserid == usert:
                tpass=input("Enter Password: ")
                if tpass == passwt:

                    print("\nOperation Used")                           
                    print("\n1.Accept Student Details\n2.Display Student Details\n3.Search Student Details\n4.Delete Details of students\n5.Update Student Details\n6.Exit")
                    cha=input("Enter Choice:-")

                    if cha =="1":

                        while True:
                            print("\n")
                            print("Accept Student Details")
                            name=input("Enter name: ")
                            while True:
                                rollNo=input("Enter rollNo: ")
                                if rollNo.isdigit() == True:
                                    rollNo = int(rollNo)
                                    break
                                else:
                                    print("Invalid Input In Integer Only!!")
                            while True:
                                marks1=input("Enter marks1: ")
                                if marks1.isdigit() == True:
                                    marks1 = int(marks1)
                                    break
                                else:
                                    print("Invalid Input In Integer Only!!")
                            while True:
                                marks2=input("Enter marls2: ")
                                if marks2.isdigit() == True:
                                    marks2 = int(marks2)
                                    break
                                else:
                                    print("Invalid Input In Integer Only!!")
                            passW=input("Enter passW: ")
                            obj.acceptStudentDetails(name,rollNo,marks1,marks2,passW)


                            print("\n1.New Entry\n2.Exit")
                            ch2=input("Enter Choice:-")
                            
                            if ch2 =="1":
                                continue
                            elif ch2 =="2":
                                print("Thank You")
                                break
                            else:
                                print("Invalid Input")

                    elif cha =="2":

                        while True:
                            print("Wanna Display Student Details")
                            obj.displaytable(l)
                            print("\n1.Yes\n2.Exit")
                            des=(input("Enter Choice: "))
                            if des == "1":
                                continue
                            elif des == "2":
                                print("Thank You!!!!")
                                break
                            else:
                                print("Invalid")

                    elif cha =="3":                
                        print("\nWanna Search Student Details\n")
                        
                        while True:
                            print("\n1.Search \n2.Exit")
                            se=input("Enter Choice: ")
                            if se == "2":
                                print("Ending...")
                                break
                            while True:
                                roll=input("Enter Rollno: ")
                                if roll.isdigit() == True:
                                    roll = int(roll)
                                    break
                                else:
                                    print("Enter Integer Value Only!!")
                            for i in range(l.__len__()):
                                if roll == l[i].rollNo:
                                    print("\n Student Found\n")
                                    s=obj.search(roll)
                                    obj.display(l) 
                            while True:
                                
                                if se == "1":
                                    break
                        
                                else:
                                    print("Invalid")

                    elif cha =="4":
                        while True:
                            print("Delete Student Details")
                            while True:
                                
                                rn=input("Enter RollNo: ")
                                if rn.isdigit() == True:
                                    rn = int(rn)
                                    break
                                else:
                                    print("Invalid Try Again !!!!!!!")

                                
                            obj.delete(rn)                       
                            print("List After Changes")
                            obj.displaytable(l)
                            print("\n1.Wanna Delete Again\n2.Exit")
                            ch3=input("Enter Choice: ")
                            if ch3 == "1":
                                continue
                            elif ch3 == "2":
                                print("Changes Applied!")
                                break
                            else:
                                print("Invalid,Try Again!!!!")
                                
                    elif cha =="5":
                        while True:
                            print("Update Student Details")
                            while True:
                                rno=input("Enter Rollno: ")
                                if rno.isdigit() == True:
                                    rno = int(rno)
                                    break
                                else:
                                    print("Invalid Try Again !!!!!!!")
                            while True:
                                rno1=input("Enter New Rollno: ")
                                if rno1.isdigit() == True:
                                    rno1 = int(rno1)
                                    break
                                else:
                                        print("Invalid Try Again !!!!!!!")   
                            print("After Changes Being Applied..")
                            obj.update(rno,rno1)
                            obj.displaytable(l)
                            print("\n1.Update Again\n2.Exit")
                            choice=input("Enter Choice: ")
                            if choice == "1":
                                continue
                            elif choice == "2":
                                print("Changes Had Been Made...")
                                break
                            else:
                                print("Invalid,Try Again!!!")
                    elif cha =="6":
                        print("Exit")
                        break
                    else:
                        print("Invalid Choice")
                else:
                    print("Invalid Password")
            else:
                print("Invalid Userid!!!Try Again")
                print("\n1.Enter Again\n2.Exit")
                choice=input("Enter Choice: ")
                if choice == "1":
                    continue
                elif choice == "2":
                    break       
        elif ch =="2":

            while True:

                print("Loging Into Student Page.......")
                   
                while True:
                    dlogin=input("Enter Rollno: ")
                    if dlogin.isdigit() == True:
                        dlogin = int(dlogin)
                        break
                    else:
                        print("Invalid!!,Try Again")
                for i in range(l.__len__()):
                    if dlogin == l[i].rollNo:
                        
                        while True:
                            dpassw=input("Enter Password: ")
                            if dpassw.isdigit() == True:
                                dpassw = int(dpassw)
                                break
                            else:
                                print("Invalid!!,Try Again")
                        if dpassw == l[i].passW:
                            print("Your Details Are As Below...")
                            ron1=l[i].rollNo
                            obj.search(ron1)
                            obj.display(l)
                break
    
        else:
            print("Invalid Input")
            break
for i in range(l.__len__()):
    print("\n\nStudent",i+1)
    print("\nName: ",l[i].name)
    print("RollNo: ",l[i].rollNo)
    print("Marks1: ",l[i].marks1)
    print("Marks2: ",l[i].marks2)
    print("PassWord: ",l[i].passW)            