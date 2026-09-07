# Ask the user for a string and create a dictionary containing the frequency of each character.
sentence = input('Enter a sentence : ')
frequency = {}
for i in sentence:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)