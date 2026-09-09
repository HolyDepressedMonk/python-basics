# Find the index of the first occurrence of target.
arr = [4, 2, 7, 2, 9, 2]
target = 2

def firstOccurrence(arr, target):
    for idx, num in enumerate(arr):
        if num == target:
            return idx
    return -1

print(firstOccurrence(arr, target))
        