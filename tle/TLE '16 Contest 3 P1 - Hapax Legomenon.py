import collections

n = input()
ans = collections.defaultdict(int)
count = 0

for i in xrange(n):
    word = raw_input()
    ans[word] += 1

for word in ans:
    if ans[word] == 1:
        count += 1

print count
