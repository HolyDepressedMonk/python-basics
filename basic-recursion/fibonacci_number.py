"""
Fibonacci of Nth term. using recursion only.
Fibonacci numbers are the sum of last two digits.
i.e :- 0,1,1,2,3,5,8,13,21,34,55....
example:
N = 5
output = 0 1 1 2 3
"""

def fibonacci(N):
    if N <= 1:
        return N

    last = fibonacci(N - 1)
    slast = fibonacci(N - 2)
    return last + slast

N = 6
print(fibonacci(N))