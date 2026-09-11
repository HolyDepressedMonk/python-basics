# Return the count of positive, negative and zero values.
arr = [4, -2, 0, 7, -5, 0, 3]

def countValues(arr):
    pos = 0
    neg = 0
    zero = 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    return [pos, neg, zero]

print(countValues(arr))