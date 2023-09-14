import math
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
n = int(input())
print(fibonacci(n))

"""
or you can try this one->

n = int(input())
fib = []
fib.append(1)
fib.append(2)
for i in range(3, n):
    fib.append(fib[i - 1] + fib[i - 2])
print(fib[n - 1])

"""