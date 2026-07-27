"""
 Given an array, we have to find the largest
 element in the array. 
 Example 1:
  
Input:
 arr[] = {2, 5, 1, 3, 0}  
Output:
 5  
Explanation:
  
5 is the largest element in the array
"""

# Bruthe Force Approach. Time Complexity is O(NlogN)
# In simple words, here we sort everything first, then pick the largest one.

def sortArr(arr):
    arr.sort()
    return arr[-1]

arr = [2, 4, 5, 1, 6, 0]
print(f"Largest Element in the array {arr} is {sortArr(arr)}")


# Optimal Approach. Time Complexity is O(N)
# just scanning the list and remebering the largest one.

def sortArr2(arr, n):
    largest_element = arr[0]

    for i in range(1, n):    
        if arr[i] > largest_element:
            largest_element = arr[i]
    
    return largest_element 

arr2 = [1, 2, 10, 16, 77, 45, 6, 90]
n = len(arr2)
print(f"Largest Element in the array {arr} is {sortArr2(arr2, n)}")
