num = int(raw_input())


for i in xrange(num):
    word = raw_input()
    start = time.time()
    length = len(word)
    suffixes = []
    for j in xrange(length):
        suffixes.append(word[j:])

    suffixes.sort()
    count = len(suffixes[0]) + 1
    for j in xrange(length - 1):
        word1 = suffixes[j]
        word2 = suffixes[j+1]
        count += len(word2)
        subtract = 0
        if len(word1) < len(word2):
            for k in xrange(len(word1)):
                if word1[k] == word2[k]:
                    subtract = k + 1
                else:
                    break
        else:
            for k in xrange(len(word2)):
                if word2[k] == word1[k]:
                    subtract = k + 1
                else:
                    break
            
        count -= subtract
    print count
