import sys, fractions

raw_input = sys.stdin.readline
n, m = map(int, raw_input().split())
lists = map(int, raw_input().split())
segTree = [0]*4*n
MAX = 1e10

def makeTree(tree, numbers, lowIndex, highIndex, pos):
    group = []
    if lowIndex == highIndex:
        #minimum, GCD, number of elements equal to GCD
        tree[pos] = [numbers[lowIndex], numbers[lowIndex], 1]
        return

    mid = (lowIndex + highIndex) / 2
    makeTree(tree, numbers, lowIndex, mid, 2*pos+1)
    makeTree(tree, numbers, mid+1, highIndex, 2*pos+2)
    group.append(min(tree[2*pos+1][0], tree[2*pos+2][0]))
    group.append(fractions.gcd(tree[2*pos+1][1], tree[2*pos+2][1]))
    group.append(0)
    if group[1] == tree[2*pos+1][1]:
        group[2] += tree[2*pos+1][2]
        
    if group[1] == tree[2*pos+2][1]:
        group[2] += tree[2*pos+2][2]

    tree[pos] = group
    return

def update(tree, lowIndex, highIndex, pos, index, value):
    group = []
    if lowIndex == highIndex:
        tree[pos] = [value, value, 1]
        return
    
    
    mid = (lowIndex + highIndex) / 2
    if index <= mid:
        update(tree, lowIndex, mid, 2*pos+1, index, value)
    else:
        update(tree, mid+1, highIndex, 2*pos+2, index, value)

    group.append(min(tree[2*pos+1][0], tree[2*pos+2][0]))
    group.append(fractions.gcd(tree[2*pos+1][1], tree[2*pos+2][1]))
    group.append(0)
    if group[1] == tree[2*pos+1][1]:
        group[2] += tree[2*pos+1][2]
        
    if group[1] == tree[2*pos+2][1]:
        group[2] += tree[2*pos+2][2]

    tree[pos] = group
    return

def query(tree, qLow, qHigh, lowIndex, highIndex, pos, qType):
    if qLow <= lowIndex and qHigh >= highIndex:
        #completely in range
        if qType == "M":
            return tree[pos][0]
        elif qType == "G":
            return tree[pos][1]
        else:
            return (tree[pos][1], tree[pos][2])

    if qLow > highIndex or qHigh < lowIndex:
        #nothing in range
        if qType == "M":
            #return maximum value
            return MAX
        elif qType == "G":
            #return any GCD
            return "Anything"
        else:
            #return any amount of numbers equal to GCD
            return "Anything"

    mid = (lowIndex + highIndex) / 2
    val1 = query(tree, qLow, qHigh, lowIndex, mid, 2*pos+1, qType)
    val2 = query(tree, qLow, qHigh, mid+1, highIndex, 2*pos+2, qType)
    if qType == "M":
        return min(val1, val2)
    elif qType == "G":
        if val1 == "Anything":
            return val2
        elif val2 == "Anything":
            return val1
        else:
            return fractions.gcd(val1, val2)
    else:
        if val1 == "Anything":
            return val2
        elif val2 == "Anything":
            return val1
        else:
            GCD = fractions.gcd(val1[0], val2[0])
            total = 0
            if val1[0] == GCD:
                total += val1[1]

            if val2[0] == GCD:
                total += val2[1]

            return (GCD, total)
    

makeTree(segTree, lists, 0, n - 1, 0)

for i in xrange(m):
    op, left, right = raw_input().split()
    left, right = int(left), int(right)

    if op == "C":
        update(segTree, 0, n - 1, 0, left - 1, right)
    elif op == "M":
        print query(segTree, left - 1, right - 1, 0, n - 1, 0, "M")
    elif op == "G":
        print query(segTree, left - 1, right - 1, 0, n - 1, 0, "G")
    else:
        print query(segTree, left - 1, right - 1, 0, n - 1, 0, "Q")[1]
    
