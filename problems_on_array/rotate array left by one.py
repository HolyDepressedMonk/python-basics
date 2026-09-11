# Rotate Array Left by One
arr = [1, 2, 3, 4, 5]

def rotateLeftOne(arr):
    if len(arr) <= 1:
        return arr

    first = arr[0]

    for idx in range(1, len(arr)):
        arr[idx-1] = arr[idx]
    arr[-1] = first
    return arr

print(rotateLeftOne(arr))