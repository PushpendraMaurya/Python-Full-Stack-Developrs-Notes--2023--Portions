print("Start")

print("10/_____")
try:
    x = 10
    y = input("Enter Number: ")
    if y == 0:
        assert x/y

    else:
        print(x/y)
except ZeroDivisionError:
    print("Cant's divide by zero")

except:
    print("Input only in str")
    

print("Stop")