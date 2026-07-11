"""
Using Recursion to print the numbers from 1 to N.
"""

# Forward Recursion

class Solution:
    def printNumbers(self, current):
        if current < 1:
            return
        
        print(current, end=" ")

        self.printNumbers(current - 1)

sol = Solution()
n = 10

print('\nForward Recursion')
sol.printNumbers(n)
print()

# Backward Recursion

class Backsolution:
    def printNumbers(self, current):
        if current < 1:
            return
        
        self.printNumbers(current - 1)

        print(current, end=" ")

backsol = Backsolution()
n = 10
print('\nBackward Recursion')
backsol.printNumbers(n)
print()
