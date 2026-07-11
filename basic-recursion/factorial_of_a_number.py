"""
Factorial of a number
n = 5
output = 5x4x3x2x1 = 120
"""

# Iterative approach

class Solution1:
    def factorial(self, n):
        total = 1
        for i in range(1, n+1):
            total *= i
        return total

# Recursive approach

class Solution2:
    def factorial(self, N):
        if N == 1:
            return 1
        return N * self.factorial(N-1)

obj = Solution2()
n = int(input('Enter a number : '))
print(obj.factorial(n))