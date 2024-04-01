n = input()
order = map(int, raw_input().split())
parents = [0]
nextParents = [0]
indexes = [0]*(n+1)
previous = []
count = 0

for i in xrange(1, n+1):
    compl = i & -i
    parents.append(i + compl)
    nextParents.append(i - compl)

for i in xrange(n):
    add = 0
    index = order[i]
    while index > 0:
        add += indexes[index]
        index = nextParents[index]

    previous.append(add)
    index = order[i]
    while index <= n:
        indexes[index] += 1
        index = parents[index]

for index, value in enumerate(order):
    if previous[index] < index - previous[index]:
        count += previous[index]
    else:
        count += index - previous[index]

print count
