"""
A B C D E 
A B C D 
A B C 
A B 
A
"""

for i in reversed(range(1, 6)):
    for j in range(i):
        print(chr(ord('A')+j), end=" ")
    print()