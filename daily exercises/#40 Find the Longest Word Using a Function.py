# Find the Longest Word Using a Function

def longestWord(sentence):
    words = sentence.split(' ')
    longest = max(words, key=len)
    return longest

sentence = 'Python programming is interesting'
print(longestWord(sentence))