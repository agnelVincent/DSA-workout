
def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [i for i in arr[:-1] if i<=pivot]
    right = [i for i in arr[:-1] if i>pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([6,4,8,9,7,10,1,3,2,5]))