import re
str="Exam123ple for meta 1character3544s i45n 123regular 1Expression"
res=re.findall("[0-9][0-9][0-9]",str)
print(res)