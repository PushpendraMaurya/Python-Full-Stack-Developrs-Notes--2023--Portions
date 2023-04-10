'''
# bottle = "water"

# if "water" in bottle:
#     print("yes ")

# else:
#     print("aymania bottle in watter")


cup = " "

var1  = "sugar"

var2 = "water"

var3 = "teapowder"

ready = var1,var2,var3 


if var1 and var2  in ready:
    # print("tea ready")
    if ready:
        print("tea is ready")

else:
    print("tea is not rady")




'''

# exam questions 


'''a = [1,2,3,4,5,6,7]
g = iter(a)
next(g)
for i in g:
    print(i)
    next(g)
    next(g)'''



# output 2 5 

'''x = 10 
y = 8
assert x>y 'X too small  '''

# output  assertion error


'''a = (1,2,4,3,8,9)
a1 = [a[i]  for i in range(0,len(a),2)]
print(a1)
'''
# output [1, 4, 8]

# set([[1,2],[3,4]])

'''set([1,2,2,3,4]) #correct'''

'''set((1,2,3,4)) # correct'''

'''{1,2,3,4}  # correct'''
# print(set)'''


'''test = {1:'a',2:'b',3:'c'}
test = {}
print(len(test))'''

#output 0

'''import math 
try:
    print(math.sqrt(81),end="")
except:
    print(0,end="")
finally:
    print(2,end="")'''

# output is 9.02
'''
s1 = {1,2,3}
s2 = {3,4,5,6}
s1.difference(s2)
s2.difference(s1)

print(s2)'''

# output #1,2 and 4,5,6

'''class demo(dict):
    def __test__(self,key):
        return []
a = demo()
a['test'] = 7
print(a)'''

# output  True

'''test = {1:"a",2:"b",3:"c"}
test = {}
print(len(test))'''

# output 0

'''a = [5,5,6,7,7,7]
b = set(a)
def test(lst):
    if lst in b:
        return 1
    
    else:
        return 0
for i in filter(test,a):
    print(i,end=" ")
'''

# output = 5 5 6 7 7 7 

'''
a,b,c = 1,2,3
a,b,c'''
# print(a,b,c)


'''a = (1:"a",2:"b",3:"c")
del a 
print(a)'''



'''my_tuple = (1,2,3,4,5)
my_tuple.append(5,6,7)
print len(my_tuple)'''

# output error 

'''test = {1:"a",2:"b",3:"c"}
test = {}
print(len(test))'''

# output 0

'''class demo(dict):
    def __test__(self,key):
        return []

a = demo()
a['test'] = 7
print(a)
'''
# output {'test': 7}


'''a = (1,2)
b = (3,4)
c = a+b

print(c)'''

# output (1, 2, 3, 4)

'''s1.issubset(s1)
if s1 = {1,2,3}

error outout '''

'''try:
    print(x)
except:
    print("an expeasdfasfg")


output = an expeasdfasfg'''

'''t = (1,2,3,4)
t[1:3]
print(t)'''

'''
count = {}
count[(1,2,4)] = 5
count[(4,2,1)] = 7
count[(1,2)] = 6
count[(4,2,1)] = 2
tot = 0
for i in count:
    tot = tot+count[i]
print(len(count) + tot)'''

# output 16

'''t = (1,2,4,8,9)
[t[i] for i in range(0,len(t),2)]

print(t)'''

# output   (1, 2, 4, 8, 9)

# a = dict()
# a[1]
# print(a)


# write the program to check water in bottle 