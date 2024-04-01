n = int(raw_input())
dict1 = {}

for i in xrange(1, n+1):
    dict1[i] = int(raw_input())

r = int(raw_input())

for i in xrange(r):
    s, e = map(int, raw_input().split())
    ans = dict1.items()
    ans.sort(key = lambda x: x[0], reverse = True)
    ans.sort(key = lambda x: abs(s - x[1]))
    best = ans[0][0]
    dict1[best] = e
    print best
