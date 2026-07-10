"""
Armstrong number

n = 153
output = True
explanation = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
"""

def amrstrong(num):
    num_length = len(str(num))
    sum = 0
    dup = num
    while num > 0:
        ld = num % 10
        sum = (ld**num_length) + sum
        num //= 10
    if dup == sum:
        return True
    else:
        return False

n = 0
print(f'Is Number {n} Armstrong : {amrstrong(n)}')
