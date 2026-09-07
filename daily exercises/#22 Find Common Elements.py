# Create a list containing the elements that appear in both lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
new_list = []
for num1 in list1:
    for num2 in list2:
        if num1 == num2:
            new_list.append(num1)
print(new_list)