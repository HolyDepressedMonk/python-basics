"""
1             1 
1 2         2 1 
1 2 3     3 2 1 
1 2 3 4 4 3 2 1
"""

for i in range(1, 5):
    for j in range(i):
        print(j+1, end=" ")
    for k in range(1, 5-i): # inner loop space after j
        print(" ", end=" ")
    for l in range(1, 5-i): # inner loop space before m
        print(" ", end=" ")
    for m in reversed(range(i)):
        print(m+1, end=" ")
    print()