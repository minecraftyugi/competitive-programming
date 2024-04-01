import sys

raw_input = sys.stdin.readline
n, m = map(int, raw_input().split())
infected = set()

for i in xrange(m):
    lists = map(int, raw_input().split())[1:]
    possible = set(lists)
    if 1 in possible:
        infected.add(1)
    if len(infected & possible) != 0:
        infected.update(possible)

print len(infected)
infected = sorted(infected)
print " ".join(map(str, infected))
