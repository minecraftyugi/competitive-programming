import sys, math
raw_input = sys.stdin.readline

s = int(raw_input())
carA = 0
carB = 0
listA = [99]
listB = [99]

def leave(num):
    remove = int(math.floor(num * (b / 100.0)))
    new = num - remove
    return new

for i in xrange(s):
    a, b = map(int, raw_input().split())
    listA = map(leave, listA)
    print listA
    listB = map(leave, listB)
    print listB
    check1 = int(math.floor(carA * (float(b) / 100)))

"""
1
1 20
"""
