# Create a reversed list using a loop.
numbers = [1, 2, 3, 4, 5]

# this method only works with Ordered list.

# rev_numbers = []
# numbers.sort(reverse=True)
# for num in numbers: 
#     rev_numbers.append(num)
# print(rev_numbers)

# Slicing method works with Ordered and Unordered List.

rev_num = numbers[::-1]
print(rev_num)