def initialSum(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10  
    return sum_digits

n = int(input("Enter the number: "))  
sum_digits = initialSum(n)

while sum_digits >= 10:
    sum_digits = initialSum(sum_digits)

print(f"The digital root of {n} is {sum_digits}")
