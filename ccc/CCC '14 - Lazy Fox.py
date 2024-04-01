import sys, math
raw_input = sys.stdin.readline
num = int(raw_input())
dict1 = {}
maxDist = 0
maxNode = ""
prevNode = (0, 0)
count = 1

for i in xrange(num):
    line = map(int, raw_input().split())
    x = line[0]
    y = line[1]
    distance = math.sqrt(float((0 - x)**2 + (0 - y)**2))
    if distance > maxDist:
        maxDist = distance
        maxNode = (x, y)

    dict1[(x, y)] = []

for key in dict1.keys():
    x = key[0]
    y = key[1]
    dict1[key] = [((thing[0], thing[1]), math.sqrt(float((x - thing[0])**2 + (y - thing[1])**2))) for thing in dict1.keys() if thing != key]
    dict1[key].sort(key = lambda x: x[1])
    pass

#maxDist += 1
print dict1, "/n"
print maxDist, maxNode
while 1:
    node = dict1[maxNode]
    if node == []:
        break
    while 1:
        if node == []:
            break
        possible = node[-1]
        neighbour = possible[0]
        dist = possible[1]
        #print neighbour, dist
        if dist >= maxDist:
            node.pop(-1)
            continue
        if prevNode == maxNode:
            node.pop(-1)
            continue
        break
    print dist, neighbour
    prevNode = maxNode
    maxNode = neighbour
    maxDist = dist
    count += 1
