def encode(wordList, lengthList, currentList, currentWord):
    new = []
    
    for word in wordList:
        letter = word[0]
        if len(currentWord) < lengthList[0]:
            currentWord += letter
        else:
            currentList.append(currentWord)
            lengthList.pop(0)
            currentWord = letter

        if len(word) != 1:
            new.append(word[1:])

    if len(new) == 0:
        return currentList + [currentWord]
    
    return encode(new, lengthList, currentList, currentWord)

def decode(wordList, lengthList, currentWord):
    index = 0
    wordPos = 0

    while 1:
        wordPos %= len(lengthList)
        letter = currentWord[index]
        word = wordList[wordPos]
        if len(word) != lengthList[wordPos]:
            word += letter
            wordList[wordPos] = word
            wordPos += 1
        else:
            wordPos += 1
            continue
        
        index += 1

        if index == len(currentWord):
            break
    
    return wordList

for i in xrange(10):
    a = raw_input()
    words = raw_input().split()
    lengths = []
    for word in words:
        lengths.append(len(word))
    
    if a == "encode":
        print " ".join(encode(words, lengths, [], ""))
    else:
        string = "".join(words)
        lists = [""for i in xrange(len(lengths))]
        print " ".join(decode(lists, lengths, string))
