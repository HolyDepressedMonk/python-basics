"""
 Given an array, we have found the number of occurrences 
 of each element in the array.

 Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	            5  2
                15  1
Explanation: 10 occurs 3 times in the array
	      5 occurs 2 times in the array
              15 occurs 1 time in the array

Example2: 
Input: arr[] = {2,2,3,4,4,2};
Output: 2  3
	           3  1
               4  2
Explanation: 2 occurs 3 times in the array
	     3 occurs 1 time in the array
             4 occurs 2 time in the array
"""

# Optmial Approach

from collections import defaultdict
# we use defaultdict so python does the initialization automatically.
# Without defaultdict, in a normal dictionary,
# we had to initialize a key before we can increment it.

class Solution:
    def Frequency(self, arr, n):
        freq_map = defaultdict(int)

        # Traverse the array and count frequencies
        for i in range(n):
            freq_map[arr[i]] += 1
        
        # items() gives the key value pair
        for key, value in freq_map.items():
            print(key, value)


sol = Solution()
arr = [10, 5, 10, 5, 15, 10]
n = len(arr)
sol.Frequency(arr, n)