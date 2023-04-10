import re 

#findall
#search
#split
#sub

str="Akash"
x=re.findall("Aka",str)
print(x)

x=re.search("sh",str)
print(x)
print(x.start())
print(x.span())
print(x.string)

x=re.split("a",str)
print(x)

x=re.sub("h","",str)
print(x)
