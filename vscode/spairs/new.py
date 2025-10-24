def lastword(my_input):
    lis = list(my_input.split(' '))
    length = len(lis)
    return lis[length-1]

my_input = input("wtf do you want? ")
print(lastword(my_input.strip()))