class Trial:
    def __init__(self,name,number,place):
        self.name = name
        self.number = number
        self.place = place    
    
    
    @classmethod
    def acceptDetails(cls,name,number,place):
        ob=cls(name,number,place)
        l.append(ob)  .023
        

    def displaytable(self,l):
        print("No\tName\tNumber\tPlace")
        for i in range(l.__len__()):
            print(f"{i+1}\t{l[i].name}\t{l[i].number}\t{l[i].place}")


l=[]

obj=Trial("","","")