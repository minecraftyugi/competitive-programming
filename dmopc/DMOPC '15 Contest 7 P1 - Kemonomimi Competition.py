n = input()
lists = map(int, raw_input().split())
dict1 = {}
maximums = []
thing = []

for i in xrange(1, 5):
    dict1[i] = lists[i-1]
    
for i in xrange(n):
    i, p, s, t = map(int, raw_input().split())
    maximums.append(s)
    thing.append((i, p, s, t))

maximum = 180 - max(maximums)

for group in thing:
    i, p, s, t = group
    if p == 10:
        print 0
        continue

    if dict1[i] * t <= maximum:
        print 10 - p
    else:
        print "The kemonomimi are too cute!"
