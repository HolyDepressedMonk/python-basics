# Find the longest word without using max().
words = ["cat", "elephant", "dog", "tiger", "butterfly"]
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)