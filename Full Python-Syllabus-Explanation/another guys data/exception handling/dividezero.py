class DivideZeroError(Exception):
    pass

try:
    a = int(input("Enter Number: "))
    if a == 0:
        raise DivideZeroError
except DivideZeroError:
    print("Zero Cannot Be Used ")
    print()