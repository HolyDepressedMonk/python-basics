# Move the last element to the beginning.
# Try doing this without using a built-in rotation function.
numbers = [1, 2, 3, 4, 5]
last_num = numbers.pop()
numbers.insert(0, last_num)
print(numbers)