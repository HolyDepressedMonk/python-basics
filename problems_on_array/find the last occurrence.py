# find the index of the last occurrence of target.
arr = [4, 2, 7, 2, 9, 2]
target = 2

def lastOccurrence(arr, target):
    for idx in range(len(arr) - 1, -1, -1):
        if arr[idx] == target:
            return idx
    return -1

print(lastOccurrence(arr, target))
