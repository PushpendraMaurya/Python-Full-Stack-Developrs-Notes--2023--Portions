


class User_Error(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return(repr(self.value))


try:
    raise (User_Error("User not defined"))
except User_Error as us:
    print("New Exception Occured: ",us.value)
    print(User_Error)