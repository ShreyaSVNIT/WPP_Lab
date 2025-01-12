#addition

"""a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print("Sum=", a + b) """

#factorial

n = eval(input("Enter a number: "))
fact = 1
for i in range(1,n) :
    fact *= i
print("Factorial=", fact)

#swap without third variable

a = eval(input("Enter a number: "))
b = eval(input("Enter a number: "))
print("Before swapping=", a, b)
a = a + b
b = a - b
a = a - b
print("After swapping=", a, b)

#table of any no.

a = eval(input("Enter a number: "))
for i in range(a) :
    print(f"{a} * {i} = {a * i}")


#reverse of a no

num = eval(input("Enter a number: "))
rev = 0, digit = 0
while num > 0:
    digit = num % 10                  
    rev_num = rev_num * 10 + digit  
    num //= 10                      

print("Reversed number: ", rev_num)
