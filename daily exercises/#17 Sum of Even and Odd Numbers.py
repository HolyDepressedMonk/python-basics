'''
Find:

Sum of all even numbers
Sum of all odd numbers

Expected:

Even sum: 20
Odd sum: 16
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_sum = 0
odd_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print(f'Even sum: {even_sum}\nOdd sum: {odd_sum}')