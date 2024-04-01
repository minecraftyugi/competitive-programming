import sys
n, m = map(int, raw_input().split())
dict1 = [[]for i in xrange(n+1)]
dict2 = [0 for i in xrange(n+1)]
dict2[1] = 1.0

for i in xrange(m):
    a, b = map(int, raw_input().split())
    dict1[a] += [b]

for i in xrange(1, n+1):
    if dict1[i] != []:
        percent = dict2[i] / len(dict1[i])

    for j in dict1[i]:
        dict2[j] += percent
        
for i in xrange(1, n+1):
    if dict1[i] == []:
        print dict2[i]
