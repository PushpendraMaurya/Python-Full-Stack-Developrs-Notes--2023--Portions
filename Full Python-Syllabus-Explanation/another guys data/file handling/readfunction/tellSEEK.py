# tell function tells the current position of cursor in the given file
# with open("hello.txt","r") as o:
#     print(o.tell())
#     print(o.read())
#     print(o.tell())







with open("hello.txt","r") as o:
    print(o.tell())
    print(o.read(2))
    print(o.tell())
    o.seek(6)
    print(o.tell())
    print(o.read())