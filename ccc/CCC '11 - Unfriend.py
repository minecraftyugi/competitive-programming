from collections import *
from itertools import *
num = int(raw_input())
dict1 = {}
count = [[]]

for i in xrange(1, num+1):
    dict1[i] = []

for i in xrange(1, num):
    number = int(raw_input())
    dict1[number].append(i)

def paths(connections, graph):
    newpaths = []
    delete = []
    for i in connections:
        for j in xrange(len(i)):
            if graph[i[j]] != []:
                delete.append(i)
                break
    for i in connections:
        newpaths.append(i)
        numList = []
        for j in i:
            numList.append(j)
        for j in i:
            if graph[j] == []:
                continue
            if graph[j][0] in i:
                continue
            graphList = graph[j]
            for number in graphList:
                numList.append(number)

        numList = list(OrderedDict.fromkeys(numList))
        numList.sort()
        newpaths.append(tuple(numList))
               
    for i in delete:
        newpaths.pop(newpaths.index(i))
        
    newpaths = list(OrderedDict.fromkeys(newpaths))

    if sorted(newpaths) == sorted(connections):
        return connections
    else:
        return paths(newpaths, graph)

start = [(x,) for x in dict1.keys() if x is not num]
answer = paths(start, dict1)

for i in xrange(1,len(answer)+1):
    lists = list(combinations(answer, i))
    for j in lists:
        thing = [number for numbers in j for number in numbers]
        if sorted(OrderedDict.fromkeys(thing)) not in count:
            count.append(sorted(OrderedDict.fromkeys(thing)))

print len(count)
