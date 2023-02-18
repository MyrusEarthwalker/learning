#optimized version
def bubble_sort(arr):
    iterations = 0
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            iterations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
    return arr, iterations

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_sort(arr))