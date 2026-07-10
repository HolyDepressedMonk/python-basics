"""
Palindrome Number
for example
number = 121
return True
number = 123
return False
"""

def palindromeNumber(n):
    reversed_number = 0
    dup = n
    while n > 0:
        temp = n % 10
        reversed_number = (reversed_number * 10) + temp
        n = n // 10
    if reversed_number == dup:
        return True
    else:
        return False

number = 121
print(f'is the number "{number}" palindrome? : {palindromeNumber(number)}" ')
    