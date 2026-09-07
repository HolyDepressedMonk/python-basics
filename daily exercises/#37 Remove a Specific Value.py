# Remove a Specific Value, Create a new list with all occurrences of 2 removed.
numbers = [5, 2, 8, 2, 10, 2, 7]
new_numbers = [num for num in numbers if num != 2]
print(new_numbers)