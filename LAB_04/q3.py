import math 

def growth(n) :
    height = 1
    for i in range (1,n+12) :
        if i % 2 != 0 : 
            height *= 2
        else : 
            height += 1
    return height

t = int(input("no of test cases: "))
for i in range(t) : 
    n = int(input("Enter the number: "))
    print(growth(n))

