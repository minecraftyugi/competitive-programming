m = input()
q = input()
dp = [1e9 for i in xrange(q)]
people = [0 for i in xrange(q)]
pairs = []
ans = []

for i in xrange(q):
    name = raw_input()
    time = input()
    pairs.append((name, time))

for i in xrange(q):
    maximum = 0
    for j in xrange(m):
        if i + j < q:
            maximum = max(maximum, pairs[i+j][1])
            if i == 0:
                if maximum < dp[i+j]:
                    dp[i+j] = maximum
                    people[i+j] = (i, i+j)
            else:
                if maximum + dp[i-1] < dp[i+j]:
                    dp[i+j] = maximum + dp[i-1]
                    people[i+j] = (i, i+j)

start = q - 1
while start != -1:
    left, right = people[start]
    lists = []
    for i in xrange(left, right+1):
        lists.append(pairs[i][0])

    ans.append(lists)
    start = left - 1

ans.reverse()
print "Total Time:", dp[-1]
for group in ans:
    print " ".join(group)
