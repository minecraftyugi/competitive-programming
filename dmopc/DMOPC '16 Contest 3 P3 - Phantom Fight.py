import sys

raw_input = sys.stdin.readline
n, m = map(int, raw_input().split())
ghosts = [0]*(n+1)
ghosts[0] = m
max_index = 1
for i in xrange(1, n+1):
    symbols, magic = map(int, raw_input().split())
    index = 1
    ghosts2 = ghosts[:]
    change = False
    while index <= i and index <= max_index:
        val = ghosts[index-1] - symbols
        if val >= 0:
            ghosts2[index] = max(ghosts[index], val + magic)
            if index == max_index:
                change = True

        index += 1

    if change:
        max_index += 1
        
    ghosts = ghosts2[:]

print max_index-1, ghosts[max_index-1]
