import datetime

a = datetime.datetime.now()
#prints year in full format
#print(a.strftime("%Y"))

#prints year in half format
#print(a.strftime("%y"))

#prints 42 ????
#print(a.strftime("%W"))

#prints 3 ???
#print(a.strftime("%w"))

#prints month number
#print(a.strftime("%m"))

#prints 45?????
#print(a.strftime("%M"))

#prints month in words shortcut
#print(a.strftime("%b"))

#prints month in words fullform
#print(a.strftime("%B"))

#prints day in words short
#print(a.strftime("%a"))

#prints day in words full
#print(a.strftime("%A"))

#prints date in number
#print(a.strftime("%d"))

#prints full date in dd\mm\yy
#print(a.strftime("%D"))

#prints hour in 24hour format
#print(a.strftime("%H"))

#prints hour in 12hour format
#print(a.strftime("%I"))

#prints PM
#print(a.strftime("%p"))

#prints minutes
#print(a.strftime("%M"))

#prints seconds
#print(a.strftime("%S"))

#prints miliseconds
#print(a.strftime("%f"))




#first task
#print(a.strftime("%I:%M:%S:%p"))


b = datetime.datetime(1,1,1,5,00,00)
#second task
# print(b.strftime("%I:%M:%S:%p"))


#self created task
#print(a.strftime("%Y-%m-%d"))


c = datetime.datetime(2022,12,1)

#second task
#print(c.strftime("%Y-%m-%d"))