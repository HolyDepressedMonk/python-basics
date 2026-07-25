"""
Given an array of size N. 
Find the highest and lowest frequency element. 

Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, 
i.e. the highest 
and the frequency of 15 is 1 i.e. the lowest.


Example 2:
Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, 
i.e. the highest 
and the frequency of 3 is 1 i.e. the lowest.
"""

# Optimal Approach HIGHEST

from collections import defaultdict

class Solution:
    def Frequency(self, arr, n):
        freq_map = defaultdict(int)

        for i in range(n):
            freq_map[arr[i]] += 1

        # to print the element which has highest freq
        high_freq = 0
        high_element = 0
        low_freq = float('inf') # taking infinity so every freq is smaller on first.
        low_element = 0
        print(freq_map)
        for key, value in freq_map.items():
            if value > high_freq:
                high_freq = value
                high_element = key
            if value < low_freq:
                low_freq = value
                low_element = key
        print(f'The Highest Element is "{high_element}" with frequency of "{high_freq}".')
        print(f'The Lowest Element is "{low_element}" with frequency of "{low_freq}".')

sol = Solution()
arr = [10, 5, 10, 5, 15, 10, 15, 2, 15, 15]
n = len(arr)
sol.Frequency(arr, n)