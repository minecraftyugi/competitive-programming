import string
punc = string.punctuation
capital = string.ascii_uppercase
num = int(raw_input())

for i in range(num):
    line = raw_input().split()
    for word in line:
        if word[0].decode('ascii', 'ignore').isupper():
            try:
                if word[0] in punc:
                    continue
                int(word[0])
                continue
            except ValueError:
                pass
            for thing in punc:
                word = word.replace(thing, "")
            print word
