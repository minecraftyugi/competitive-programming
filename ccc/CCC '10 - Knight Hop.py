import sys
start = raw_input()
start = list(start)
start = (int(start[0]), int(start[2]))
end = raw_input()
end = list(end)
end = (int(end[0]), int(end[2]))
dict1 = {}
shortest = 0

if start == end:
    print 0
    sys.exit()

for i in xrange(1, 9):
    for j in xrange(1, 9):
        dictList = []
        if (i + 2) >= 1 and (i + 2) <= 8 and (j + 1) >= 1 and (j + 1) <= 8:
            dictList.append((i + 2, j + 1))
        if (i + 2) >= 1 and (i + 2) <= 8 and (j - 1) >= 1 and (j - 1) <= 8:
            dictList.append((i + 2, j - 1))
        if (i - 2) >= 1 and (i - 2) <= 8 and (j + 1) >= 1 and (j + 1) <= 8:
            dictList.append((i - 2, j + 1))
        if (i - 2) >= 1 and (i - 2) <= 8 and (j - 1) >= 1 and (j - 1) <= 8:
            dictList.append((i - 2, j - 1))
        if (i + 1) >= 1 and (i + 1) <= 8 and (j + 2) >= 1 and (j + 2) <= 8:
            dictList.append((i + 1, j + 2))
        if (i + 1) >= 1 and (i + 1) <= 8 and (j - 2) >= 1 and (j - 2) <= 8:
            dictList.append((i + 1, j - 2))
        if (i - 1) >= 1 and (i - 1) <= 8 and (j + 2) >= 1 and (j + 2) <= 8:
            dictList.append((i - 1, j + 2))
        if (i - 1) >= 1 and (i - 1) <= 8 and (j - 2) >= 1 and (j - 2) <= 8:
            dictList.append((i - 1, j - 2))
        dict2 = {(i,j) : dictList}
        dict1.update(dict2)

def knight(start, end, graph, count=1):
    paths = []
    if end in start:
        return count

    for pos in start:
        options = graph[pos]
        for option in options:
            paths.append(option)

    start = set(paths)
    count += 1

    return knight(start, end, graph, count)

starter =  dict1[start]
print knight(starter, end, dict1)
