with open("hello.txt","r") as o:
    word = 0
    char = 0
    lines = 0
    for i in o:
        lines +=1
        i = i.strip("\n")
        char += len(i)
        l = i.split()
        word += len(l)

print("Words =  ",word)
print("Lines =  ",lines)
print("Chars =  ",char)