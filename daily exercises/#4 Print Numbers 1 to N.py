# Ask the user for n and print numbers from 1 to n.
num = int(input('Enter a number : '))
if num > 0:
    for i in range(1, num+1):
        print(i)
else:
    print('Enter a number greater than 0.')
