"""
Count Digits of a Number

Example 1:
n = 12345
output = 5

Example 2:
n = 7789
output = 4
"""

def countDigits(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count

number = 12345
print(f'Number of digits in {number} : {countDigits(number)} ')
