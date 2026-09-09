# Find the second-largest element without sorting.
arr = [49, 10, 25, 47, 42, 18, 29, 44, 50]
largest = 0
sec_largest = 0
for el in arr:
    if el > largest:
        sec_largest = largest
        largest = el
print(sec_largest)