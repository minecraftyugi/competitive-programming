word = ""
while word != "quit!":
    word = raw_input()
    length = len(word)
    wordList = list(word)
    if (length > 4) and (word[length - 3] != "a") and (word[length - 3] != "e") and (word[length - 3] != "i") and (word[length - 3] != "o") and (word[length - 3] != "u") and (word[length - 3] != "y") and (word[length - 2] == "o") and (word[length - 1] == "r"):
        wordList.insert(length - 1, 'u')
        print "".join(wordList)
    else:
        if word != "quit!":
            print word
        else:
            break
