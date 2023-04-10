# accesing data from the file by using read function
# with open("hello.txt","r") as t:
#     data = t.read(100)
#     print(data)







# readline function reads one single line
# with open("hello.txt") as o:
#     data = o.readline()
#     print(data,end = "")







# readlines function reads all lines in a list
# with open("hello.txt") as o:
#     data = o.readlines()
#     print(data)

# with open("hello.txt") as o:
#     data = o.readlines()
#     for i in data:
#         print(i,end="")






f = open("hello.txt","r")
for line in f:
    print(line,end="")
f.close()






























