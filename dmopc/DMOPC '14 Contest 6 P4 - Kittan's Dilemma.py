import sys, bisect
raw_input = sys.stdin.readline

n, m = map(int, raw_input().split())
list1 = []
list2 = []
pre1 = [0]
pre2 = [0]
maximum = 0

for i in xrange(n):
    s, p = map(int, raw_input().split())
    
    if p == 1:
        list1.append(s)
    else:
        list2.append(s)
    
list1.sort()
list2.sort()

for i in xrange(len(list1)):
    pre1.append(list1[i] + pre1[-1])

for i in xrange(len(list2)):
    pre2.append(list2[i] + pre2[-1])

for index, value in enumerate(pre1):
    if index == 0:
        continue

    if value > m:
        break

    position = bisect.bisect_right(pre2, m - value)
    
    if position != 0:
        maximum = max(maximum, index + 2 * (position - 1))
    else:
        maximum = max(maximum, index)

for index, value in enumerate(pre2):
    if index == 0:
        continue

    if value > m:
        break

    position = bisect.bisect_right(pre1, m - value)

    if position != 0:
        maximum = max(maximum, index * 2 + position - 1)
    else:
        maximum = max(maximum, index * 2)

print maximum
