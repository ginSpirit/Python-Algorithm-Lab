import math

def mergeSort(a, l, r):
    
    if l < r:
        m = math.floor((l+r)/2)
        mergeSort(a, l, m)
        mergeSort(a, m + 1, r)
        merge(a, l, m, r)

def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(0, n1):
        L[i] = a[l + i]

    for j in range(0, n2):
        R[j] = a[m + 1 + j]

    L[n1] = math.inf
    R[n2] = math.inf

    i = 0
    j = 0
    for k in range(l, r + 1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1

n = int(input())
A = list(map(int, input().split()))[:n]
mergeSort(A, 0, len(A) - 1)

for i in A:
    print(i, end= " ")