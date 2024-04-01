import sys
raw_input = sys.stdin.readline
n = int(raw_input())
energy = map(int, raw_input().split())
length = map(int,raw_input().split())
energy.sort()
length.sort(reverse=True)
count = 0

for i in xrange(n):
    count += energy[i] * length[i]

print count
