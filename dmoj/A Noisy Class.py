import sys, collections

raw_input = sys.stdin.readline
dict1 = collections.defaultdict(set)
dict2 = {}

n = int(raw_input())
num = int(raw_input())

for i in xrange(num):
    points = map(int, raw_input().split())
    a = points[0]
    b = points[1]
    dict1[a].add(b)

for i in dict1.keys():
    dict2[i] = set([i])

for i in dict1:
    for j in dict1[i]:
        try:
            node = dict2[j]
            if dict2[i] != dict2[j]:
                new = dict2[i].union(dict2[j])
                for num in new:
                    dict2[num] = new
            else:
                print "N"
                sys.exit()
        except KeyError:
            pass

print "Y"
