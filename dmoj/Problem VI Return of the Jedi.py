s,e,r = map(int, raw_input().split())
dict1 = {i:[] for i in xrange(1,5)}
dict2 = {}
count = 0

for i in xrange(s):
    w,x,y = map(int, raw_input().split())
    dict1[w].append((x, y))

for i in xrange(e):
    x,y = map(int, raw_input().split())
    dict2[(x,y)] = []

for num in dict1:
    for point in dict1[num]:
        x1 = point[0]
        y1 = point[1]
        for ewok in dict2:
            x2 = ewok[0]
            y2 = ewok[1]
            if ((x2-x1)**2 + (y2-y1)**2)**.5 <= r:
                dict2[ewok].append(num)

for i in dict2.values():
    if len(set(i)) > 1:
        count += 1

print count
