import sys
raw_input = sys.stdin.readline
line = map(int, raw_input().split())
m = line[0]
n = line[1]
q = line[2]
numList = [0] + map(int, raw_input().split())
parents = [0]
nextParent = [0]
ans = [0 for i in xrange(n+1)]

for i in xrange(1, n+1):
    numBits = len(str(bin(i))) - 2
    compl = abs(i - (1 << numBits))
    and1 = i & compl
    parent = i - and1
    parents.append(parent)
    parent2 = i + and1
    nextParent.append(parent2)

for i in xrange(1, n+1):
    number = numList[i]
    ans[i] += number
    start = i
    while 1:
        go = nextParent[start]
        if go <= n:
            ans[go] += number
            start = go
        else:
            break

print ans

for i in xrange(q):
    thing = map(int, raw_input().split())
    op1 = thing[0]
    if op1 == 1:  
        left = thing[1]
        right = thing[2]
        difference = thing[3]
        ans[left] += difference
        while 1:
            go = nextParent[left]
            if go <= n and go <= right:
                ans[go] += difference
                left = go
            else:
                break

        print ans

