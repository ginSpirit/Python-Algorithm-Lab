def bubble_Sort(array):
    for i in range (len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

n = int(input())
array = list(map(int, input().split()))[:n]
bubble = bubble_Sort(array)
print(bubble)