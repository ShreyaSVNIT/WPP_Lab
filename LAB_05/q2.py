import math

def isSquare(x):
    s = int(math.sqrt(x))
    return s * s == x 


T = int(input())
for _ in range(T):
    n = int(input())
    fibo = isSquare(5 * n * n + 4) or isSquare(5 * n * n - 4)
    if fibo:
        print("IsFibo")
    else:
        print("IsNotFibo")
