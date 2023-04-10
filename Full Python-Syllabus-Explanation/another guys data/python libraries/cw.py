import cal as c

a = 10
b = 20

print(c.l)

#Object Created
print(c.calc.add(a,b))


c.mul(a,b)

#Object Not Created: Which will give error 
print(c.Calc.add(a,b))