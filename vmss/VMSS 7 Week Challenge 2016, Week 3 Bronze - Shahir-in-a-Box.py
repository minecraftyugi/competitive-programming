import sys
raw_input = sys.stdin.readline
n = int(raw_input())
list1 = []
list2 = []

for i in xrange(n):
    x, y = map(int, raw_input().split())
    list1.append(x)
    list2.append(y)

list1.sort()
list2.sort()

print (list1[-1] - list1[0])*(list2[-1] - list2[0])
