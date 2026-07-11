"""
Sum of first Natural N numbers.
n = 5
output = 1+2+3+4+5 = 15
"""

# Brute Force by iterating from 1 to N and adding to total.

class Solution1:
    def sumOfNaturalNumbers(self, N):
        total = 0
        for i in range(1, N+1):
            total += i
        return total
    
n = 6
sol = Solution1()
result = sol.sumOfNaturalNumbers(n)
# print(result)


# By Formula N(N+1)/2

class Solution2:
    def sumOfNaturalNumbers(self, N):
        return (N * (N + 1)) //  2

sol2 = Solution2()
# N = int(input('Enter a number : '))
# print(sol2.sumOfNaturalNumbers(N))


# By Recursion

class Solution3:
    def sumOfNaturalNumbers(self, N):
        if N == 1:
            return 1
        return N + self.sumOfNaturalNumbers(N-1)

sol3 = Solution3()
print(sol3.sumOfNaturalNumbers(2))