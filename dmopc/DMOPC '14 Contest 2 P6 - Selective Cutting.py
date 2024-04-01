import sys
raw_input = sys.stdin.readline
n = int(raw_input())
masses = [0] + map(int, raw_input().split())
queries = int(raw_input())
parent = [0]
nextParent = [0]
ans = [0 for i in xrange(n+1)]
queue = []
order = [0 for i in xrange(queries)]

for i in xrange(1, n+1):
    number = i
    length = i.bit_length()
    compl = abs(number - (1 << length))
    and1 = number & compl
    parent1 = number - and1
    parent += [parent1]
    parent2 = number + and1
    nextParent += [parent2]

for i in xrange(queries):
    a, b, q = map(int, raw_input().split())
    queue += [(a,b,q,i)]

queue.sort(key = lambda x: x[2], reverse=True)
list1 = list(enumerate(masses))
list1.sort(key = lambda x: x[1], reverse=True)
index = 0

for i in xrange(queries):
    a, b, q, place = queue[i]
    newIndex = index
    for j in xrange(index, n+1):
        treeIndex, tree = list1[j]
        if tree >= q:
            ans[treeIndex] += tree
            while nextParent[treeIndex] <= n:
                treeIndex = nextParent[treeIndex]
                ans[treeIndex] += tree

            newIndex += 1
        else:
            index = newIndex
            break

    start = a
    end = b + 1
    ans1 = ans[start]
    ans2 = ans[end]
    while start > 0:
        start = parent[start]
        ans1 += ans[start]

    while end > 0:
        end = parent[end]
        ans2 += ans[end]

    num = ans2 - ans1
    order[place] = num

for i in order:
    print i
