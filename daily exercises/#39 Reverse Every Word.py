# Reverse each word individually while keeping the word order the same.
sentence = "hello world python"
# expected : olleh dlrow nohtyp
rev_sentence = [x[::-1] for x in sentence.split(' ')]
print(' '.join(rev_sentence))