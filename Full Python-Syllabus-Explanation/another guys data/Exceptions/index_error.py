try:
    i=0
    l = [1,2,3,4,5,6]
    while i < 7:
        print(l[i])
        i += 1
except IndexError as Index:
    print(Index)
    print("Done")