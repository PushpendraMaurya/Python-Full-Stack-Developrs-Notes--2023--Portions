#we created a Exception which will execute when the balnce is less than 2000
class BalnaceExceptionError(Exception):
    pass

def check():
    money = 10000
    withdraw = 9000
    try:
        balance = money - withdraw
        if balance <= 2000:
            raise BalnaceExceptionError("Insufficient Balance")
    except BalnaceExceptionError as b:
        print(b)
        print(BalnaceExceptionError)

check()