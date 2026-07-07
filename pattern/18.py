"""
E 
D E 
C D E 
B C D E 
A B C D E
"""

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(chr(ord('F')-j), end=" ")
    print()