# Create two lists:

# one containing even numbers
# one containing odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_list, even_list = [], []
for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
print('Even: ', even_list)
print('Odd: ', odd_list)