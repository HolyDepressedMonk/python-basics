"""
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * *
"""
for i in reversed(range(1, 6)):
    for j in range(i):
        print('*', end=" ")
    for j in range(5-i): # Top left space
        print(' ', end=" ")
    for k in range(5-i): # Top right space
        print(' ', end=" ")
    for l in range(i):
        print('*', end=" ")
    print()


for i in range(1, 6):
    for j in range(i):
        print('*', end=" ")
    for j in range(5-i): # Bottom left space
        print(' ', end=" ")
    for k in range(5-i): # Bottom right space
        print(' ', end=" ")
    for l in range(i):
        print('*', end=" ")
    print()