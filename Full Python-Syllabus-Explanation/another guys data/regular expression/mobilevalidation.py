import re

number=input("Enter valid Number:-")

pattern=re.compile("(0|91)?[-\s]?[6-9][0-9]{9}$")
if pattern.match(number):
    print(f"{number}is valid")
else:
    print("is not valid")