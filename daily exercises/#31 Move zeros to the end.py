# Create a new list where all zeros are moved to the end.
# [NOTE] : this can be rearrage within the same list which is more optimal way and consuming less space complexity. 
numbers = [0, 5, 0, 2, 8, 0, 3]
new_list = []
count = 0
for num in numbers:
    if num != 0:
        new_list.append(num)
    else:
        count += 1
new_list.extend([0] * count)
print(new_list)
# print(count)