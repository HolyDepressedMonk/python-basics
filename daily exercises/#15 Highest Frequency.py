# Create a frequency dictionary and print the element that appears the most.
numbers = [10, 5, 10, 15, 10, 5]
frequency = {}
for i in numbers:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
# print(list(frequency.keys()))
highest = max(frequency, key=frequency.get)
print(highest)