# Use a loop to count how many numbers are even.
numbers = [10, 3, 7, 8, 12, 5, 6]
count = 0
for i in numbers:
    if i % 2 == 0:
        count += 1
print(count)