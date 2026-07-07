"""
      A 
    A B A 
  A B C B A 
A B C D C B A
"""

for i in range(1, 5):
    for j in range(1, 5-i):
        print(" ", end=" ")
    for k in range(1, i+1):
        # print(k, end=" ")
        print(chr(ord('A')+ k-1), end=" ")
    for l in range(i-1, 0, -1): # for this to understand refer below.
        print(chr(ord('A')+ l-1), end=" ")
    print()

# This will generate a sequence like this.
"""

1 
2 1 
3 2 1
"""
# it will simply prints numbers from (i-1) down to 1
# for i in range(1, 5):
#     for l in range(i-1, 0, -1):
#         print(l, end=" ")
#     print()