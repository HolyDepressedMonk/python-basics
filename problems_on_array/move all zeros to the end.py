# Maintain the relative order of the non-zero elements.
arr = [0, 1, 0, 3, 12]

def moveZero(arr):
    write = 0
    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write] = arr[read]
            write+=1
    while write < len(arr):
        arr[write] = 0
        write += 1
    return arr

print(moveZero(arr))