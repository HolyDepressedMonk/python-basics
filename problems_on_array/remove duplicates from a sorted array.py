# Modify the array so that each value appears only once.
arr = [1, 1, 2, 2, 3, 4, 4]

def removeDuplicates(arr):
    if len(arr) == 0:
        return arr
    slow = 1
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow-1]:
            arr[slow] = arr[fast]
            slow+=1
    return arr[:slow]

print(removeDuplicates(arr))

