'''
Create a new list containing each number only once.

Expected:

[1, 2, 3, 4, 5]

Don't use set() yet.
'''
numbers = [1, 2, 2, 3, 4, 4, 5, 1]
new_list = [] 
numbers.sort()
count = 0
for num in numbers:
    if num != count:
        count = num
        new_list.append(num)
print(new_list)