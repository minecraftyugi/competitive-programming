import sys
raw_input = sys.stdin.readline
dict1 = {}

n = input()

for i in xrange(1, n+1):
    line = map(int, raw_input().split())
    dict1[i] = line[1:]

q = input()
print dict1

for i in xrange(q):
    point = int(raw_input())
