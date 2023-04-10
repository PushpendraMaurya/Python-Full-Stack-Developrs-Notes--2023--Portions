import re

#a-z
#0-9
#.-(one time in email)
# @ (one time only)
# . (4th position from end)

email_condn="^[a-z]+[\.-]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

while True:
    user_email=input("Enter Your Email:-")
    if re.search(email_condn,user_email):
        print("Rigth Mail")
        break

    else:
        print("Wrong Mail")