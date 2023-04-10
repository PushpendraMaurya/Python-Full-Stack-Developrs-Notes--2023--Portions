# print("start")

# x = -1
# if x < 0:
#     raise TypeError("Sorry")

# print("Stop")    





print("Start")

print("10/_____")
try:
    x = 10
    y = input("Enter Number: ")
    if y == 0:
        raise ZeroDivisionError("Zero Can't be divided by any number")

    else:
        print(x/y)
except (ZeroDivisionError,TypeError) as s:
    print(s)
    print("Hiiii")

print("Stop")