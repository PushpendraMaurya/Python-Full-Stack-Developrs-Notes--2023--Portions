from module import *


obj.acceptProfDetails("Saurav","Kanto",18,"Researcher","sm123","5852")
obj.acceptProfDetails("Bunty","Kanto",20,"Researcher","ss123","5852")
obj.acceptProfDetails("Vishal","Kanto",20,"Researcher","vm123","5852")
obj.acceptProfDetails("Akash","Kanto",22,"Researcher","ad123","5852")

obj1.acceptTrainDetails("Saurav","Karlos","Pikachu",18,"sm456","1234")
obj1.acceptTrainDetails("Bunty","Karlos","Pichu",20,"ss456","1234")
obj1.acceptTrainDetails("Vishal","Karlos","Aron",20,"vm456","1234")
obj1.acceptTrainDetails("Akash","Karlos","Pikachu",22,"ad456","1234")

obj2.acceptPokDetails("Pikachu","pika2","thunder","normal","Chu",100)
obj2.acceptPokDetails("Pichu","pika1","thunder","normal","Chuchu",100)
obj2.acceptPokDetails("Raichu","pika3","thunder","normal","Chucha",100)
obj2.acceptPokDetails("Onix","on","rock","normal","On",100)



while True:
    print("\n1.Admin Login\n2.Professor Login\n3.Trainer Login\n4.Exit")
    login=input("Enter Choice: ")
    if login == "1":
        usr_id_a = "Admin"
        pass_a = "1234"
        print("\n\nLoging Into Admin Page...\n")        
        user_id = input("Enter UserId: ")
        if user_id == usr_id_a:                
            password = input("Enter Password: ")
            if password == pass_a:
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
                print("Invalid Password")
        else:
            print("Invalid UserId")
                    

           
    elif login == "2":       
        print("\n\nLoging Into Proffesor Page...\n")
              
        user_id_p=input("Enter UserId: ")
        for i in range(l.__len__()):
            if user_id_p == l[i].p_user_id:
                password_p=input("Enter Password: ")
                if password_p == l[i].p_password:
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
                    print("Invalid Password")
                    
        else:
            print("Invalid UserId")
            
        
    elif login == "3":
        print("Logining into trainer page...")
        usr_id_t = input("Please enter your  : ")
        for i in range(o.__len__()):
            if usr_id_t == o[i].userid_t:
                pass_t = input("Please enter your password")
                if pass_t == o[i].password_t:
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
                    print("Invalid Password")
            else:
                print("Invalid Userid")
    elif login == "4":
        print("\n\nThanks For Using Our Pokedex Services..\n")
        break
    else:
        print("Invalid Choice!!")

for i in range(l.__len__()):
    print("\n\nProfessor",i+1)
    print("\nName: ",l[i].name)
    print("Region: ",l[i].region)
    print("Age: ",l[i].age)
    print("Speciality: ",l[i].speciality)
    print("User Id: ",l[i].p_user_id)
    print("Password: ",l[i].p_password) 


for i in range(o.__len__()):
   
    print("\nName: ",o[i].name_t)
    print("Region: ",o[i].region_t)
    print("Stater Pokemon: ",o[i].st_pokemon)
    print("Age: ",o[i].age_t)
    print("User Id: ",o[i].userid_t)
    print("Password: ",o[i].password_t)   