# Write a function to Count how many uppercase and lowercase letters there are. and Ignore spaces.
text = "Hello WORLD Python"

def countCase(text):
    uc, lc = 0, 0
    for char in text:
        if char.isupper():
            uc += 1
        elif char.islower():
            lc += 1
    print('upper case count:', uc)
    print('lower case count:', lc)

countCase(text)
