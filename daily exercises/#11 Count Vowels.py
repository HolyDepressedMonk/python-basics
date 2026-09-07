# Ask the user for a string and count how many vowels (a, e, i, o, u) it contains.
string = input('Enter a string : ')
count = 0
for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
print(count)