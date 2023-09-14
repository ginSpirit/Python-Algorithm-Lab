import math
def fibonacci(n):
    fib = [n+2]
    fib[0] = 0
    fib[1] = 1
    for i in range (2,n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
n = int(input())
print(fibonacci(n))

