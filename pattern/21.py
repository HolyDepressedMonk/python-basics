"""
* * * * 
*     * 
*     * 
* * * *
"""

for i in range(4):
    for j in range(4):
        # i and j (rows and colums) there first and last index is what needed.
        if i == 0 or i == 4 - 1 or j == 0 or j == 4 - 1:
            print("*", end=" ")
        else:
            print(' ', end=" ")
    print()