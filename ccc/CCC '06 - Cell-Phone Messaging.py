dict1 = { 1 : ("a","d","g","j","m","p","t","w"),
          2 : ("b","e","h","k","n","q","u","x"),
          3 : ("c","f","i","l","o","r","v","y"),
          4 : ("","","","","","s","","z")
        }
while True:
    word = raw_input()
    time = 0
    if word == "halt":
        break
    for i in xrange(len(word)):
        if word[i] in dict1[1]:
            time += 1
            pos = dict1[1].index(word[i])
        if word[i] in dict1[2]:
            time += 2
            pos = dict1[2].index(word[i])
        if word[i] in dict1[3]:
            time += 3
            pos = dict1[3].index(word[i])
        if word[i] in dict1[4]:
            time += 4
            pos = dict1[4].index(word[i])
        if i < len(word) - 1:
            if (word[i + 1] in dict1[1] and pos == dict1[1].index(word[i + 1])):
                time += 2
                continue
            if (word[i + 1] in dict1[2] and pos == dict1[2].index(word[i + 1])):
                time += 2
                continue
            if (word[i + 1] in dict1[3] and pos == dict1[3].index(word[i + 1])):
                time += 2
                continue
            if (word[i + 1] in dict1[4] and pos == dict1[4].index(word[i + 1])):
                time += 2
                continue
    print time
