"""
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1
"""

for i in range(1, 5+1):
    for j in range(i):
        # if % 2 then 0, if not then 1
        print((i + j) % 2, end=" ")
    print()