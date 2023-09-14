def insertion_sort(array):
    for i in range (1, len(array)):
        current_value = array[i]
        j = i-1 
        while j>=0 and array[j]>current_value:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = current_value
    return array

n = int(input())
array = list(map(int, input().split()))[:n]
insertion_sort(array)
for i in array:
    print(i, end=" ")