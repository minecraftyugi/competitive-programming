import bisect
n = input()
w1 = list("elpsycongroo")
w2 = list("tuturu")
w3 = list("superhacker")
w4 = list("myfork")

for i in xrange(n):
    line = raw_input()
    dict1 = {chr(i):[] for i in xrange(97,123)}
    for index, letter in enumerate(line):
        dict1[letter] += [index]
        
    ans = []

    count = 0
    index = 0
    for letter in w1:
        count += 1
        pos = bisect.bisect_left(dict1[letter], index)
        if pos == len(dict1[letter]):
            break

        index = dict1[letter][pos]
        if count == len(w1):
            ans += ["Okabe"]

    count = 0
    index = 0
    for letter in w2:
        count += 1
        pos = bisect.bisect_left(dict1[letter], index)
        if pos == len(dict1[letter]):
            break

        index = dict1[letter][pos]
        if count == len(w2):
            ans += ["Mayuri"]

    count = 0
    index = 0
    for letter in w3:
        count += 1
        pos = bisect.bisect_left(dict1[letter], index)
        if pos == len(dict1[letter]):
            break

        index = dict1[letter][pos]
        if count == len(w3):
            ans += ["Daru"]

    count = 0
    index = 0
    for letter in w4:
        count += 1
        pos = bisect.bisect_left(dict1[letter], index)
        if pos == len(dict1[letter]):
            break

        index = dict1[letter][pos]
        if count == len(w4):
            ans += ["Kurisu"]

    if len(ans) == 0:
        print "SERN spy!"
    else:
        print " or ".join(ans)
