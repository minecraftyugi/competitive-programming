import sys
raw_input = sys.stdin.readline

n = input()
q = input()
parent = [0]*251
child = [0]*251
tree = [[[0 for i in xrange(251)]for i in xrange(251)]for i in xrange(251)]
total = 0

for i in xrange(1, 251):
    compl = i & -i
    parent[i] = i + compl
    child[i] = i - compl

def treeAdd(x, y, z, val):
    while x < n + 1:
        y1 = y
        while y1 < n + 1:
            z1 = z
            while z1 < n + 1:
                tree[x][y1][z1] += val
                z1 = parent[z1]

            y1 = parent[y1]

        x = parent[x]
        
    return

def treeSum(x1, y1, z1):
    total = 0
    x = x1
    while x:
        y = y1
        while y:
            z = z1
            while z:
                total += tree[x][y][z]
                z = child[z]

            y = child[y]

        x = child[x]
       
    return total

def difference(x1, y1, z1, x2, y2, z2):
    a = treeSum(x2, y2, z2)
    b = treeSum(x1-1, y2, z2)
    c = treeSum(x2, y1-1, z2)
    d = treeSum(x2, y2, z1-1)
    e = treeSum(x1-1, y1-1, z2)
    f = treeSum(x1-1, y2, z1-1)
    g = treeSum(x2, y1-1, z1-1)
    h = treeSum(x1-1, y1-1, z1-1)
    return a-b-c-d+e+f+g-h

for i in xrange(q):
    l = raw_input().split()
    l2 = map(int, l[1:])
    if l[0] == "C":
        x, y, z, v = l2
        diff = v - difference(x, y, z, x, y, z)
        treeAdd(x, y, z, diff)
    else:
        x1, y1, z1, x2, y2, z2 = l2
        total += difference(x1, y1, z1, x2, y2, z2)

print total
