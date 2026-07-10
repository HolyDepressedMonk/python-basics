"""
greatest common divisor
n1 = 20
n2 = 15

output = 5 (GCD)
"""
# This is Euclidean Algorithm (optimal)
# Repeatedly subtract the smaller number from the larger number until one of them becomes 0. The other number will be GCD.
def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    if a == 0:
        return b
    else:
        return a


num1 = 22
num2 = 25
print(min(num1, num2))
print(f'GCD of {num1} and {num2} is : {gcd(num1, num2)}')