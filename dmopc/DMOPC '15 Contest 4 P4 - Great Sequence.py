import bisect, collections, sys
raw_input = sys.stdin.readline

n, k, q = map(int, raw_input().split())
lists = map(int, raw_input().split())
sums = [0]
dict1 = collections.defaultdict(list)

for index, value in enumerate(lists):
    sums += [value + sums[-1]]
    dict1[value] += [index]
    
for i in xrange(q):
    a, b, x, y = map(int, raw_input().split())
    if sums[y] - sums[x-1] <= k:
        print "No"
    else:
        if x > y:
            x, y = y, x
        if a not in dict1:
            print "No"
            continue
        
        posA = bisect.bisect_left(dict1[a], x-1)
        if posA == len(dict1[a]):
            print "No"
            continue
        
        if dict1[a][posA] >= x - 1 and dict1[a][posA] < y:
            if b not in dict1:
                print "No"
                continue
            posB = bisect.bisect_left(dict1[b], y)
            if posB == len(dict1[b])+1:
                print "No"
                continue
            
            if dict1[b][posB-1] >= x - 1 and dict1[b][posB-1] < y:
                print "Yes"
                continue

        print "No"
