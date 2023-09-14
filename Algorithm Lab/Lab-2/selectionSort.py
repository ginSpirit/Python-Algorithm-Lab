import math #not necessary

def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

n = int(input())
array = list(map(int, input().split()))[:n]
selection_sort(array)
for i in array:
    print(i, end=" ")