# Given a list of numbers, Create a dictionary showing the frequency
# Then print the number with the highest frequency.

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(max(frequency.values()))
