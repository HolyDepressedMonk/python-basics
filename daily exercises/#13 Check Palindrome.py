# Write a function that checks whether a string is a palindrome.
def checkPalindrome(string):
    if string == string[::-1]:
        print('Palindrome')
    else:
        print('Not Palindrome')

checkPalindrome('madam')
checkPalindrome('hello')