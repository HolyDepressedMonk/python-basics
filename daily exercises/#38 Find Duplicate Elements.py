# Find Duplicate Elements, Find which numbers appear more than once. Try not to print the same duplicate multiple times.
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
numbers.sort()
prev_el = numbers[0]
dup_list = []
for num in numbers:
    if prev_el == num and num not in dup_list:
        dup_list.append(num)
    prev_el = num
print(dup_list)