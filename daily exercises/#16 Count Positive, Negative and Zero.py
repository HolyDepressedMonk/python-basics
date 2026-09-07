'''
Count how many numbers are:

Positive
Negative
Zero

Expected:
Positive: 3
Negative: 3
Zero: 2
'''

numbers = [10, -5, 0, 7, -2, 0, 8, -10]
pos_count = 0
neg_count = 0
zero_count = 0
for i in numbers:
    if i > 0:
        pos_count += 1
    elif i < 0:
        neg_count += 1
    else:
        zero_count += 1
print(f'Positive: {pos_count}\nNegative: {neg_count}\nZero: {zero_count} ')