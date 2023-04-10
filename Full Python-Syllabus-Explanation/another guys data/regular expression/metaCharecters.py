import re

# str="Example for meta character in regular Expression"

# res=re.findall("[a-q]",str)
# print(res)

# str="Example for meta character in regular Expression"

# res=re.findall("[aes]",str)
# print(res)

# str="Example for meta character in regular Expression"

# res=re.findall("n$",str)
# print(res)

# str="Example for meta characters in regular Expression"

# res=re.findall("E.+er",str)
# print(res)

str="Example for meta characters in regular Expression"

res=re.findall("s{2}",str)
print(res)