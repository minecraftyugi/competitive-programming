num = int(raw_input())

for i in xrange(num):
    words = raw_input().split()
    for j in xrange(len(words)):
        if len(words[j]) == 4:
            words[j] = "****"

    print " ".join(words)
