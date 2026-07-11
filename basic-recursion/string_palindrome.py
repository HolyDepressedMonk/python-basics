"""
String is Palindrome or not
str = "ABCBA"
output = Palindrome

str = "MONK"
output = Not Palindrome
"""

class Solution:
    def stringPalindrome(self, i, s):
        # optimal approach (using recursion)
        # first we check if i exceed half of the string
        if i >= len(s) // 2:
            return True
        
        # if start and end characters are not equal, return False
        if s[i] != s[len(s) - i - 1]:
            return False
        
        # if charactes are same, increment i and check start+1 and end-1
        return self.stringPalindrome(i+1, s)



obj = Solution()
str1 = "maam"
print(obj.stringPalindrome(0, str1))

