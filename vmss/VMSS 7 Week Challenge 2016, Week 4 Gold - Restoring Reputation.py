import sys
d, i, r = map(int, raw_input().split())
words = raw_input().split()

if len(words) > 1:
    a, b = words
else:
    a = words[0]
    b = raw_input()
    
aLen, bLen = len(a), len(b)
lists = [[0 for x in xrange(bLen+1)]for y in xrange(aLen+1)]

for j in xrange(1, aLen+1):
    lists[j][0] = j * d

for j in xrange(1, bLen+1):
    lists[0][j] = j * i

for x in xrange(1, aLen+1):
    for y in xrange(1, bLen+1):
        if a[x-1] == b[y-1]:
            cost = 0
        else:
            cost = r

        delete = lists[x-1][y] + d
        insert = lists[x][y-1] + i
        sub = lists[x-1][y-1] + cost
        lists[x][y] = min(delete, insert, sub)
          
print lists[-1][-1]
