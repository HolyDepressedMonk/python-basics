# Find the smallest number without using min().
numbers = [10, 4, 25, 2, 18]
# numbers.sort()
# print(numbers[0])

smallest_num = numbers[0]
for num in numbers:
    if num < smallest_num:
        smallest_num = num
print(smallest_num)