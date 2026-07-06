"""
12345
1234
123
12
1
"""

for i in reversed(range(1, 6)):
    for j in range(1, i):
        print(j, end="")
    print(i)