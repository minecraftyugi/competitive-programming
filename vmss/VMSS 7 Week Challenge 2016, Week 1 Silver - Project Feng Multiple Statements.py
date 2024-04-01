import collections, sys
n = input()
ans = []

for i in xrange(n):
    num = input()
    ans += [num]

ans = collections.Counter(ans).most_common()
ans.sort(key = lambda x: x[0], reverse=True)

for a, b in ans:
    if a == 0 and ans[-1][0] == 0:
        print "Paradox!"
        sys.exit()
    if a == b:
        print a
        sys.exit()

print 0
