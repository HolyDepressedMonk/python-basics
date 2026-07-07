"""
A 
B B 
C C C 
D D D D 
E E E E E
"""

for i in range(1, 6):
    for j in range(i):
        # after '@', Capital Alphabets starts 'A', 'B', 'C'......
        print(chr(ord("@")+i), end=" ")
        # one more way to print after '@'
        # print(chr(ord("A")+i-1), end=" ")
    print()