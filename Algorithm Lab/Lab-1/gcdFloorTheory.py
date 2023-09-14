import math

def gcd_using_formula(a, b):
    if b == 0:
        return a
    else:
        return gcd_using_formula(b, a-b*math.floor(a/b))

a, b = map(int, input().split())
print(gcd_using_formula(a,b))