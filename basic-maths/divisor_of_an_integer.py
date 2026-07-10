"""
Divisor of an integer.
n = 21
output = [1, 3, 7, 21]
n = 20
output = [1, 2, 4, 5, 10, 20]
"""

# Brute Force Method (iterates over every number.)
# def divisorNumber(num):
#     emt_list = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             emt_list.append(i)
#     return emt_list
            
# n = 21
# print(int(math.sqrt(n)))
# print(int(math.isqrt(n)))
# print(f'divisor for the number {n} : {divisorNumber(n)}')

# the Optimal Approach (iterate from 1 to sqrt(n) and for every divisor found, if N/divisor is distinct, add that to the list as well.)

import math

def divisorNumber(n):
    emt_list = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            emt_list.append(i)

            if i != n // i:
                emt_list.append(n // i)
    return sorted(emt_list)

n = 20
print(f'divisor for the number {n} : {divisorNumber(n)}')