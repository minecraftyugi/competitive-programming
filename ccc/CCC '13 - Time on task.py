import sys
list1 = map(int, sys.stdin.read().strip().split('\n'))
list2 = sorted(list1[2:len(list1)])
num = list1[0]
count = 0

for i in xrange(len(list2)):
    count += list2[i]
    if count > num:
        print i
        break
