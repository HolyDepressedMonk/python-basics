# Find the largest number without using max().
numbers = [10, 25, 7, 42, 18]
# numbers.sort()
# print(numbers[-1])

largest_num = numbers[0]
for num in numbers:
    if num > largest_num:
        largest_num = num
print(largest_num)