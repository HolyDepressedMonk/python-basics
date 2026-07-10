"""
Reverse Digits of a number

also not include trailing zeros in reverse.
for example:
number = 10400
reverse = 401, not 00401.
"""

number = 1040120

def reveseNumber(n):
    reversed_number = 0
    while n > 0:
        temp = n % 10
        n = n // 10
        reversed_number = (reversed_number * 10) + temp 
    return reversed_number

print(f'Reversed number of {number} is : {reveseNumber(number)}')


