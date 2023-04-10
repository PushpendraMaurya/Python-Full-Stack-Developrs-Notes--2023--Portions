# def findMissingNumbers(n):
#     numbers = set(n)
#     length = len(n)
#     output = []
#     for i in range(1, n[-1]):
#         if i not in numbers:
#             output.append(i)
#     return output
    
# listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
# print(findMissingNumbers(listOfNumbers))

# def MissNumber(n):
#     number = set(n)
#     length = len(n)
#     output = []
#     for i in range(1, n[-1]):
#         if i not in number:
#             output.append(i)
    
#     return output


# Numbers = [1,3,4,5,6,7,8,9,11]
# print(MissNumber(Numbers))


def Solutions(n):
    number = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in number:
            output.append(i)
    
    return output


Numbers = [1,2,3,5]
print(Solutions(Numbers))