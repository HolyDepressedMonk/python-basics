"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * *
"""

for i in range(1, 5+1):
    for j in range(5-i): # inner loop for spaces
        print(' ', end=" ")
    for k in range(1, 2*i): # inner loop for stars
        print('*', end=" ")
    print()