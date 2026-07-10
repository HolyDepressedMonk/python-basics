"""
Prime Numbers, which are divisble by 1 and them itself.
"""
# Brute Force method
# def primeNumber(n):
#     emt_list = []
#     for i in range(1, n+1):
#         print(n%i)
#         if n % i == 0:
#             emt_list.append(i)
#     return emt_list

# n = 21
# print(f'Prime Numbers of number {n} : {primeNumber(n)}')


# Optimal Method (iterate from 1 to sqrt(n) and for every divisor found, if n/divisor is distinct, add that to the list as well.)
import math

def primeNumber(n):
    emt_list = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            emt_list.append(i)
        
            if i != n // i:
                emt_list.append(n // i)
    return sorted(emt_list)

n = 16
print(f'Prime Numbers of number {n} : {primeNumber(n)}')
