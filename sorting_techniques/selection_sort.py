"""
Given an array of N integers, write a program to implement the Selection sorting algorithm.

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1, 2, 3, 4, 5
"""
class Solution:
    def selectionSort(self, arr):
        for i in range(len(arr)-1):
            mini = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[mini]:
                    mini = j
                    arr[i], arr[mini] = arr[mini], arr[i]
        print("After sorting")
        print(arr)

arr1 = [13,46,24,52,20,9]
obj = Solution()
print("Before sorting")
print(arr1)
obj.selectionSort(arr1)