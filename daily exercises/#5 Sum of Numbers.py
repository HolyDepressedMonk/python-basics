# Ask the user for n and calculate : 1 + 2 + 3 + ... + n
num = int(input('Enter a number : '))
sum = 0
if num > 0:
    for i in range(1, num+1):
        sum = sum + i
else:
    print("Enter a number greater than 0.")
print(sum)