with open("hello.txt","r") as o:
    data = o.read()
    print(o.mode)
    print(o.encoding)     
    print(data)