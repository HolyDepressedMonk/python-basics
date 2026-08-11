# CHECK IF ARRAY IS SORTED OR NOT (WITHOUT USING SORT METHOD)

class Solution:
    def checkSort(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True

obj = Solution()
arr = [1,2,3,4,6,5]
print(obj.checkSort(arr))