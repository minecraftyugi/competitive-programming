word = raw_input("Enter a string...")
word = word.upper()
wordLen = len(word)
wordList = list(word)
print "* " + ' '.join(wordList) + " *"
x = " "

for i in xrange(wordLen):
    y = x
    x = y + "* "
    
for i in xrange(wordLen):
    print word[wordLen - i - 1] + x + word[i]
    
wordList = wordList[::-1]
print "* " + ' '.join(wordList) + " *"
