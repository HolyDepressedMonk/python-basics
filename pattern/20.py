"""
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 *
"""

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    for k in range(5-i): # Top left space
        print(" ", end=" ")
    for l in range(5-i): # Top right space
        print(" ", end=" ")
    for m in range(i):
        print("*", end=" ")
    print()

for i in reversed(range(1, 6)):
    for j in range(i):
        print("*", end=" ")
    for k in range(5-i): # Bottom left space
        print(' ', end=" ")
    for l in range(5-i): # Bottom right space
        print(' ', end=" ")
    for m in range(i):
        print("*", end=" ")
    print()