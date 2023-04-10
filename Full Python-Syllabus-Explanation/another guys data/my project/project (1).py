class Professer:
    def __init__(self,name,region,age,speciality,p_user_id,p_password):
        self.name = name
        self.region = region
        self.age = age
        self.speciality = speciality
        self.p_user_id = p_user_id
        self.p_password = p_password

    @classmethod
    def acceptProfDetails(cls,name,region,age,speciality,p_user_id,p_password):
        ob=cls(name,region,age,speciality,p_user_id,p_password)
        l.append(ob)

    def displaytable(self,l):
        print("No\tName\tRegion\tage\tSpeciality\tUserId\tPassword")
        for i in range(l.__len__()):
            print(f"{i+1}\t{l[i].name}\t{l[i].region}\t{l[i].age}\t{l[i].speciality}\t{l[i].p_user_id}\t{l[i].p_password}")

    def display(self,l):
        print("Name: ",l[i].name)
        print("Region: ",l[i].region)
        print("Age: ",l[i].age)
        print("Speciality: ",l[i].speciality)
        print("Userid: ",l[i].p_user_id)
        print("Password: ",l[i].p_password)

    def search(self,userid):
        for i in range(l.__len__()):
            if(l[i].p_user_id == userid):
                return i

    def delete(self,user):
        j=obj.search(user)
        del l[j]

class Trainer:
    def __init__(self,name_t,region_t,st_pokemon,age_t,userid_t,password_t):
        self.name_t = name_t
        self.region_t = region_t
        self.st_pokemon = st_pokemon
        self.age_t = age_t
        self.userid_t = userid_t
        self.password_t = password_t

    @classmethod
    def acceptTrainDetails(cls,name_t,region_t,st_pokemon,age_t,userid_t,password_t):
        oc=cls(name_t,region_t,st_pokemon,age_t,userid_t,password_t)
        o.append(oc)   

    def displaytable(self,o):
        print("No\tName\tRegion\tStater\tAge\tUserId\tPassword")
        for i in range(o.__len__()):
            print(f"{i+1}\t{o[i].name_t}\t{o[i].region_t}\t{o[i].st_pokemon}\t{o[i].age_t}\t{o[i].userid_t}\t{o[i].password_t}") 

    def display(self,o):
        print("\nName: ",o[i].name_t)
        print("Region: ",o[i].region_t)
        print("Stater Pokemon: ",o[i].st_pokemon)
        print("Age: ",o[i].age_t)
        print("User Id: ",o[i].userid_t)
        print("Password: ",o[i].password_t)   
        
    def search(self,userid):
        for i in range(o.__len__()):
            if(o[i].userid_t == userid):
                return i

    def delete(self,user):
        k=obj1.search(user)
        del o[k]

class Pokemon:
    def __init__(self,name_p,pokemon_Id,type,rarity,nickname,level):
        self.name_p = name_p
        self.pokemon_Id = pokemon_Id
        self.type = type
        self.rarity = rarity
        self.nickname = nickname
        self.level = level

    @classmethod
    def acceptPokDetails(cls,name_p,pokemon_Id,type,rarity,nickname,level):
        od=cls(name_p,pokemon_Id,type,rarity,nickname,level)
        p.append(od)   

    def displaytable(self,p):
        print("No\tName\tId\tType\tRarity\tNickname\tLevel")
        for i in range(p.__len__()):
            print(f"{i+1}\t{p[i].name_p}\t{p[i].pokemon_Id}\t{p[i].type}\t{p[i].rarity}\t{p[i].nickname}\t\t{p[i].level}") 

    def displayp(self,p):
        print("\nName of pokemon: ",p[i].name_p)
        print("Pokemon id: ",p[i].pokemon_Id)
        print("Type: ",p[i].type)
        print("Rarity: ",p[i].rarity)
        print("Nickname: ",p[i].nickname)
        print("Level: ",p[i].level)   
        
    def searchp(self,pokid):
        for i in range(p.__len__()):
            if(p[i].pokemon_Id == pokid):
                return i

    def deletep(self,pok):
        pn=obj2.searchp(pok)
        del p[pn]
    
obj=Professer("","","","","","")
obj1=Trainer("","","","","","")
obj2=Pokemon("","","","","","")

l=[]
o=[]
p=[]


obj.acceptProfDetails("Saurav","Kanto",18,"Researcher","sm123","5852")
obj1.acceptTrainDetails("Saurav","Karlos","Pikachu",18,"sm456","1234")
obj2.acceptPokDetails("Pikachu","pika2","thunder","normal","Chu",100)



while True:
    print("\n1. Admin Login\n2. Professor Login\n3. Trainer Login\n4. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        a_login = "Admin"
        a_password = "1234"
        login_1 = input("Enter UserId: ")
        pass_1 = input("Enter Password")
        if login_1 == a_login:
        
            if pass_1 == a_password:
                while True:
                    print("\n1.Add Professor\n2.Display Professor\n3.Search Professor\n4.Delete Professor\n5.Exit")
                    prof=input("Enter Choice: ")


                    if prof == "1":
                        print("\n\nFunction Executed..\n")                                   
                        while True:
                            print("\n1.Add\n2.Exit")
                            add=input("Enter Choice: ")
                            if add == "1":
                                name=input("Enter Name Of Professor: ")
                                region=input("Enter The Region To Which The Professor Belongs: ")                    
                            
                                while True:
                                    age=input("Enter The Age Of The Professor: ")
                                    if age.isdigit() == True:
                                        age = int(age)
                                        break
                                    else:
                                        print("Invalid Input In Integer Only!!")
                                speciality=input("Enter The Specialiy: ")
                                p_user_id=input("Enter The User Id Of Professer: ")
                                p_password=input("Enter The Password of Professor")
                                obj.acceptProfDetails(name,region,age,speciality,p_user_id,p_password)
                            elif add == "2":
                                print("Changes Had Been Made")
                                break
                            else:
                                print("Invalid Choice!!")


                    elif prof == "2":
                        print("\n\nDisplaying Professor Details..\n")               
                        while True:
                            obj.displaytable(l)
                            print("\n\n1.Display Again\n2.Exit")
                            dis=input("Enter Choice: ")
                            if dis == "1":
                                continue
                            elif dis == "2":
                                print("Exited..")
                                break
                            else:
                                print("Invalid Choice!!")


                    elif prof == "3":
                        print("\n\nFunction Executed....\n")
                        while True:
                            print("\n1.Search \n2.Exit")
                            se=input("Enter Choice: ")                                            
                            if se == "1":                           

                                while True:

                                    userid=input("Enter Userid: ")                        
                                    for i in range(l.__len__()):
                                        if userid == l[i].p_user_id:
                                            print("\n Professor Found!\n")
                                            s=obj.search(userid)
                                            obj.display(l)                                                     
                                    break     
                            elif se == "2":
                                print("Ending...")
                                break                                                                    
                            else:
                                print("Invalid Choice!!!")


                    elif prof == "4":               
                        print("Delete Professor")                                           
                        while True:   
                            print("\n1.Delete\n2.Exit")
                            ch3=input("Enter Choice: ")
                            if ch3 == "1":
                                user=input("Enter Userid: ")                                                
                                obj.delete(user)                       
                                print("List After Changes")
                                obj.displaytable(l)
                            elif ch3 == "2":
                                print("Changes Applied!")
                                break
                            else:
                                print("Invalid Choice!!!")
                                

                    elif prof == "5":
                        print("\n\nChanges Had Been Made Succesfully..\n")
                        break


                    else:
                        print("Invalid Choice!!")  
                        
                              
            else:
                print("Invalid Password , Try Again!!")
        else:
            print("Invalid UserId , Try Again!!")     

    elif choice == "2":
        for i in range(l.__len__()):
            p_login = l[i].p_user_id
            p_pass = l[i].p_password

            user_p = input("Enter UserId: ")
            pass_p = input("Enter Password: ")

            if user_p == p_login:

                if pass_p == p_pass:
                    while True:
                        print("\n1.Add Trainer\n2.Display Trainer Info\n3.Search Trainer Info\n4.Delete Trainer\n5.Exit")
                        tr=input("Enter Choice: ")
                        if tr == "1":
                            while True:
                                name_t=input("Enter Name Of Trainer: ")
                                region_t=input("Enter The Region To Which The Trainer Belongs: ")
                                st_pokemon=input("Enter Stater Pokemon Of The Trainer")                                                 
                                while True:
                                    age_t=input("Enter The Age Of The Trainer: ")
                                    if age_t.isdigit() == True:
                                        age_t= int(age_t)
                                        break
                                    else:
                                        print("Invalid Input In Integer Only!!")
                                userid_t=input("Enter The User Id Of Trainer: ")
                                password_t=input("Enter The Password of Trainerr")
                                obj1.acceptTrainDetails(name_t,region_t,st_pokemon,age_t,userid_t,password_t)
                                print("\n1.Add Again\n2.Exit")
                                add=input("Enter Choice: ")
                                if add == "1":
                                    continue
                                elif add == "2":
                                    print("Changes Had Been Made")
                                    break
                                else:
                                    print("Invalid Choice!!")


                        elif tr == "2":
                            print("\n\nDisplaying Trainer Details..\n")               
                            while True:
                                obj1.displaytable(o)
                                print("\n\n1.Display Again\n2.Exit")
                                dis=input("Enter Choice: ")
                                if dis == "1":
                                    continue
                                elif dis == "2":
                                    print("Exited..")
                                    break
                                else:
                                    print("Invalid Choice!!")

                            
                        elif tr == "3":
                            print("\n\nFunction Executed....\n")
                            while True:
                                print("\n1.Search \n2.Exit")
                                se=input("Enter Choice: ")                                            
                                if se == "1":                           
                                    while True:
                                        userid=input("Enter Userid: ")                        
                                        for i in range(o.__len__()):
                                            if userid == o[i].userid_t:
                                                print("\n Professor Found!\n")
                                                t=obj1.search(userid)
                                                obj1.display(o)                                                     
                                        break     
                                elif se == "2":
                                    print("Ending...")
                                    break                                                                    
                                else:
                                    print("Invalid Choice!!!")


                        elif tr == "4":
                            print("\n\nFunction Executed\n")
                            while True:                                                                                   
                                print("\n1.Delete\n2.Exit")                    
                                ch3=input("Enter Choice: ")
                                if ch3 == "1":
                                    user=input("Enter Userid: ")                                                
                                    obj1.delete(user)                       
                                    print("List After Changes")
                                    obj1.displaytable(o)                                    
                                elif ch3 == "2":
                                    print("Changes Applied!")
                                    break
                                else:
                                    print("Invalid Choice!!!")

                                    
                        elif tr == "5":
                            print("Changes Had Been Made Successfully....")
                            break


                        else:
                            print("Invalid Choice!!!")


                else:
                    print("Invalid Password , Try Again!!!")

            else:
                print("Invalid UserId , Try Again!!!")

    elif choice == "3":
        for i in range(o.__len__()):
            t_userid = o[i].userid_t
            t_pass = o[i].password_t

            id_t = input("Enter UserId: ")
            pass_t = input("Enter Password: ")
            if id_t == t_userid:

                if pass_t == t_pass:
                    while True:
                        print("\n1.Add Pokemon\n2.Display Pokemon\n3.Search Pokemon\n4.Release Pokemon\n5.Display Trainer Data\n6.Exit")
                        tr=input("Enter Choice: ")

                        
                        if tr == "1":
                            while True:
                                name_p = input("Enter Name Of Pokemon: ")
                                pokemon_Id = input("Enter Id of pokemon: ")
                                type = input("Enter type of pokemon: ")
                                rarity = input("Enter rarity of pokemon")
                                nickname = input("Enter nickname if any")                                             
                                while True:
                                    level=input("Enter The Level Of The Pokemon: ")
                                    if level.isdigit() == True:
                                        level= int(level)
                                        break
                                    else:
                                        print("Invalid Input In Integer Only!!")
                                obj2.acceptPokDetails(name_p,pokemon_Id,type,rarity,nickname,level)
                                print("\n1.Add Again\n2.Exit")
                                add=input("Enter Choice: ")
                                if add == "1":
                                    continue
                                elif add == "2":
                                    print("Changes Had Been Made")
                                    break
                                else:
                                    print("Invalid Choice!!")


                        elif tr == "2":
                            print("\n\nDisplaying Pokemons....\n")               
                            while True:
                                obj2.displaytable(p)
                                print("\n\n1.Display Again\n2.Exit")
                                dis=input("Enter Choice: ")
                                if dis == "1":
                                    continue
                                elif dis == "2":
                                    print("Exited..")
                                    break
                                else:
                                    print("Invalid Choice!!")
                            

                        elif tr == "3":
                            print("\n\nFunction Executed....\n")
                            while True:
                                print("\n1.Search \n2.Exit")
                                se=input("Enter Choice: ")                                            
                                if se == "1":                           
                                    while True:
                                        pokid=input("Enter Pokemonid: ")                        
                                        for i in range(p.__len__()):
                                            if pokid == p[i].pokemon_Id:
                                                print("\n Pokemon Found!\n")
                                                t=obj2.searchp(pokid)
                                                obj2.displayp(p)                                                     
                                        break     
                                elif se == "2":
                                    print("Ending...")
                                    break                                                                    
                                else:
                                    print("Invalid Choice!!!")


                        elif tr == "4":
                            print("\n\nFunction Executed\n")
                            while True:                                                                                   
                                print("\n1.Release\n2.Exit")                    
                                ch3=input("Enter Choice: ")
                                if ch3 == "1":
                                    pok=input("Enter Userid: ")                                                
                                    obj2.deletep(pok)                       
                                    print("List After Changes")
                                    obj2.displaytable(p)                                    
                                elif ch3 == "2":
                                    print("Your pokemon is released!!!")
                                    break
                                else:
                                    print("Invalid Choice!!!")
                                    

                        elif tr == "5":
                            print("\n\nFunction Executed....\n")
                            while True:
                                print("\n1.Search \n2.Exit")
                                se=input("Enter Choice: ")                                            
                                if se == "1":                           
                                    while True:
                                        userid=input("Enter Userid: ")                        
                                        for i in range(o.__len__()):
                                            if userid == o[i].userid_t:
                                                print("\n Professor Found!\n")
                                                t=obj1.search(userid)
                                                obj1.display(o)                                                     
                                        break     
                                elif se == "2":
                                    print("Ending...")
                                    break                                                                    
                                else:
                                    print("Invalid Choice!!!")


                        elif tr == "6":
                            print("Thanks for using our service.....")
                            break


                        else:
                                print("Invalid Choice!!!")


                else:
                    print("Invalid Password , Try Again!!")

            else:
                print("Invalid UserId , Try Again!!")

    elif choice == "4":
        print("Thanks for using our service....")
        break

    else:
        print("Invalid Choice!!!!!")