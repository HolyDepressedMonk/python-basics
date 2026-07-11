"""
Using Recursion to print the numbers from 1 to N.
Recursion means the function calls itself in order to solve the problem by breaking it down into subproblems.

In Backward Recursion all the recursive function executes first, then the processing(here printing) happens 
in reverse order(it is called 'unwinding' also).  
"""

# Forward Recursion

class Solution:
    def printNumbers(self, current, n):
        if current > n:
            return
        
        print(current, end=" ")

        self.printNumbers(current + 1, n)

sol = Solution()
n = 10

print('\nForward Recursion')
sol.printNumbers(1, n)
print()

# Backward Recursion

class Backsolution:
    def printNumbers(self, current, n):
        if current > n:
            return
        
        self.printNumbers(current + 1, n)

        print(current, end=" ")

backsol = Backsolution()
n = 10
print('\nBackward Recursion')
backsol.printNumbers(1, n)
print()