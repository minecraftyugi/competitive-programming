import sys
lists = sys.stdin.read().strip().split('\n')
lists.pop(0)
lists = sorted(lists, key = int)

for i in lists:
    print i
