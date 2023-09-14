import math
def gcd_number(a, b):
    while b!=0:
        a, b = b, (a-b)*math.floor(a//b)
    return abs(a)

num1 = int(input("enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
result = gcd_number(num1, num2)
print(result)