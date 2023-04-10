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
        print("No\tStater Pokemon\tName\tId\tType\tRarity\tNickname\tLevel")
        for i in range(p.__len__()):
            for j in range(o.__len__()):
                print(f"{i+1}\t{o[j].st_pokemon}\t{p[i].name_p}\t{p[i].pokemon_Id}\t{p[i].type}\t{p[i].rarity}\t{p[i].nickname}\t\t{p[i].level}") 

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
