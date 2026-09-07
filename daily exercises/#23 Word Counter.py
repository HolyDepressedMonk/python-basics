'''
Ask the user to enter a sentence.
Create a dictionary containing the frequency of each word.
'''
sentence = input('Enter a sentence : ')
dic = {}
for i in sentence.split(' '):
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)