# Ask the user for n and print all prime numbers from 1 to n.
number = int(input('Enter a number : '))
for i in range(1, number+1):
    for j in range(1, i+1):
    #  and i % 2 != 0
        if i % i == 0 and i % j != 0:
            print(i)