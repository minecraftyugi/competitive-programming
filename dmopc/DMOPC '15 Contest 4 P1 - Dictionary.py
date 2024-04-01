n = input()
dict1 = {chr(x):[] for x in xrange(97,123)}

for i in xrange(n):
    word = raw_input()
    letter = word[0]
    dict1[letter] += [word]

ans = sorted(dict1.items())

for key, value in ans:
    if value != []:
        value.sort()
        print ", ".join(value)
     
