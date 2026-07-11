"""
Reversing a string
n = [1,2,3,4,5]
output = [5,4,3,2,1]
"""

class Solution:
    def reverseArray(self, n):
        # 1st method using reversed and append method.
        # emt_arr = []
        # for i in reversed(n):
        #     emt_arr.append(i)
        # return emt_arr

        # 2nd method using enumerate and indexing
        # first make emt_array same as size of n.
        # emt_arr = len(n) * [0]
        # for i, value in enumerate(n):
        #     emt_arr[len(n) - 1 - i] = value
        # return emt_arr

        # 3rd method using slicing to reverse the array. (easiest)
        n[:] = n[::-1]
        return n


obj = Solution()
n = [1,2,3,4,5]
print(obj.reverseArray(n))