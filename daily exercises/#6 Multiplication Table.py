# Ask the user for a number and print its multiplication table from 1 to 10.
num = int(input('Enter a number : '))
if num > 0:
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')