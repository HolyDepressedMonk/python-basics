# Create a dictionary containing the frequency of each number.
# Try doing it without defaultdict first.
numbers = [10, 5, 10, 15, 10, 5]
frequency = {}
for i in numbers:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)
