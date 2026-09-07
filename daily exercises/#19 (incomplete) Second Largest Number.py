# Find the second largest number. Try doing it without using sort().
numbers = [30, 25, 7, 42, 18, 10, 1]
max_first = 0
max_second = 0
for num in numbers:
    if num > max_first:
        max_first = num
    elif num < max_first and num > max_second:
        max_second = num
print(max_first)
print(max_second)