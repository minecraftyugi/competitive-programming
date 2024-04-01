import sys, bisect, collections

#lists = map(int, sys.stdin.read().strip().split('\n'))
lists = [5,100,200,150,170,50]
num1 = lists[0]
add = 0
numList = []
"""
for i in xrange(1, num1 + 1):
    number = lists[i]
    score = bisect.bisect_right(numList, number)
    if i == 1 or number >= numList[i - 2]: 
        numList.append(number)
    else: 
        numList.insert(score, number)
    add += i - score

num = add / float(num1)
print ("%.2f" % round(num,2))
"""
raw_input = sys.stdin.readline
n = int(raw_input())
segTree = [0]*4*n
dict1 = collections.defaultdict(int)
lists = []

for i in xrange(n):
    lists.append(int(raw_input()))

def makeTree(tree, numbers, lowIndex, highIndex, pos):
    group = []
    if lowIndex == highIndex:
        tree[pos] = ([numbers[lowIndex]], [lowIndex])
        return

    mid = (lowIndex + highIndex) / 2
    makeTree(tree, numbers, lowIndex, mid, 2*pos+1)
    makeTree(tree, numbers, mid+1, highIndex, 2*pos+2)

    group1 = []
    group2 = []
    left = tree[2*pos+1]
    right = tree[2*pos+2]
    minIndex = left[1][0]
    lIndex = 0
    rIndex = 0
    while lIndex < len(left[1]) or rIndex < len(right[1]):
        if lIndex == len(left[1]):
            group1.append(right[0][rIndex])
            if len(group2) == 0:
                group2.append(minIndex)
            else:
                group2.append(group2[-1] + 1)

            if group2[-1] < right[1][rIndex]:
                dict1[group1[-1]] += right[1][rIndex] - group2[-1]
                
            rIndex += 1
            continue
        
        if rIndex == len(right[1]):
            group1.append(left[0][lIndex])
            lIndex += 1
            if len(group2) == 0:
                group2.append(minIndex)
            else:
                group2.append(group2[-1] + 1)
            continue
        
        if left[0][lIndex] <= right[0][rIndex]:
            group1.append(left[0][lIndex])
            lIndex += 1
            if len(group2) == 0:
                group2.append(minIndex)
            else:
                group2.append(group2[-1] + 1)
        else:
            group1.append(right[0][rIndex])
            if len(group2) == 0:
                group2.append(minIndex)
            else:
                group2.append(group2[-1] + 1)

            if group2[-1] < right[1][rIndex]:
                dict1[group1[-1]] += right[1][rIndex] - group2[-1]
                
            rIndex += 1

    tree[pos] = (group1, group2)
    return
    
makeTree(segTree, lists, 0, n-1, 0)
ans = sum(dict1.values()) + n + 0.0
print "{0:.2f}".format(ans / n)

