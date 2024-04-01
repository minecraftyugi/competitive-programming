import sys
lists = map(int, sys.stdin.read().strip().split('\n'))
#lists = [100,6,50,30,10,10,40,50]
#lists = [100,3,150,1,1]
num = lists[0]
count = 0
weight = 0

for i in xrange(lists[1]):
    count += 1
    weight += lists[i + 2]
    if count > 4:
        weight -= lists[i - 2]
        if weight > num:
            print i
            break
    if weight > num:
        print i
        break      
    if i == lists[1] - 1:
        print i + 1
        break
