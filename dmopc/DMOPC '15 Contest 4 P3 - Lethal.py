from itertools import *
import bisect
g = input()

for i in xrange(g):
    n = input()
    if n == 0:
        print "NOT LETHAL"
        continue
    
    lists = map(int, raw_input().split())
    health, tauntHealth = map(int, raw_input().split())
    dict1 = {}
    lists2 = chain(*(combinations(lists,i)for i in xrange(1,n+1)))
    for i in lists2:
        num = reduce(lambda a,b: a + b, i)
        dict1[num] = i

    if max(dict1) <= tauntHealth:
        print "NOT LETHAL"
        continue
    else:
        ans = sorted(dict1.keys())
        pos = bisect.bisect_left(ans, tauntHealth)
        removeList = dict1[ans[pos]]
        for num in removeList:
            lists.remove(num)

        if sum(lists) < health:
            print "NOT LETHAL"
        else:
            print "LETHAL"
