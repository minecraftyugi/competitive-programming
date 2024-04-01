import sys
raw_input = sys.stdin.readline
j = int(raw_input())
a = int(raw_input())
dict1 = {}
count = 0

for i in xrange(1, j + 1):
    jersey = raw_input().strip()
    dict1[i] = jersey

for i in xrange(a):
    thing = raw_input().strip().split()
    size = thing[0]
    jnum = int(thing[1])
    print dict1
    try:
        newSize = dict1[jnum]
        if size == "M":
            if newSize != "M" and newSize != "L":
                continue
        elif size == "L":
            if newSize != "L":
                continue
        else:
            pass
    except KeyError:
        continue
    count += 1
    del dict1[jnum]
    
print count
