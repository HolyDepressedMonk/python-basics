# You are given numbers from 1 to n, but one number is missing.
# Find the missing number.
numbers = [1, 2, 3, 5, 6]
last_num = numbers[-1]
full_numbers = [num for num in range(1, last_num + 1)]
#  O(n) time, and you only loop twice (once for each sum)
print(sum(full_numbers) - sum(numbers))

# The more better way which takes even less time complexity according to DSA.
# O(n) time (only to sum the list), O(1) space (no extra data structures, don't need to create full_numbers),
print((last_num * (last_num + 1) // 2) - sum(numbers))