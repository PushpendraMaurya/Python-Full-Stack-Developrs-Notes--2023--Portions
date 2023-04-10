try:
    a = "q"
    b = 10
    print(a+b)
except TypeError as t:
    print(str(a)+str(b))
    print(TypeError)
    print(t)