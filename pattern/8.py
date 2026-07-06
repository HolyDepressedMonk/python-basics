"""
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        *
"""

for i in reversed(range(1, 5+1)):
    for j in range(5-i):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print("*", end=" ")
    print()