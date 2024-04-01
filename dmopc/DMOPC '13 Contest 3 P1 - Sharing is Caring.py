import collections
n, m = map(int, raw_input().split())
dict1 = collections.defaultdict(list)

for i in xrange(m):
    p, q = map(int, raw_input().split())
    line = raw_input()
    dict1[q].append(line)

y = input()

if y in dict1:
    for doc in dict1[y]:
        print doc
