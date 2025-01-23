test = int(input("Enter the number of test cases: "))
for i in range(test) :
    n = input("Enter the number: ")
    count = 0
    for digit in n: 
        if digit != '0':
            if int(n) % int(digit) == 0:
                count+=1
    print(count)
