"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        *
"""

for i in range(1, 5+1):
    for j in range(5-i):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print("*", end=" ")
    print()
for l in reversed(range(1, 5+1)):
    for m in range(5-l):
        print(" ", end=" ")
    for n in range(1, 2*l):
        print("*", end=" ")
    print()

    