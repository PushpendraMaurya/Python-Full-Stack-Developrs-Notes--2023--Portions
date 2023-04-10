import random

class Error(Exception):
    pass
class SmallError(Exception):
    pass
class LargeError(Exception):
    pass


num = random.randint(1,6)
print(num)

try:
    n = int(input("Enter Number: "))
    if n < num:
        raise SmallError
    elif n > num:
        raise LargeError
    else:
        print("Perfect Guess...........")
except SmallError:
    print("Guessed number is Smaller")
except LargeError:
    print("Guessed number is Larger")
