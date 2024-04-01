q = input()
dict1 = {0:1}

for i in xrange(1, 38):
    dict1[i] = 3**i
    
for i in xrange(q):
    l, r = map(int, raw_input().split())
