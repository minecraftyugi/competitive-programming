import collections, sys
raw_input = sys.stdin.readline
n = int(raw_input())
dict1 = collections.defaultdict(list)
dict2 = {}
count1 = 0
count2 = 0

for i in xrange(n):
    line = map(int, raw_input().split())
    num = line[0]
    for j in xrange(1, num + 1):
        start = line[j]
        end = line[j+1]
        if j == num:
            end = line[1]
        cost = line[-num + j -1]
        if start > end:
            start, end = end, start
        dict1[(start, end)].append(i)
        dict2[(start, end)] = cost

list1 = [i for i in dict1.keys() if len(dict1[i]) == 1]
list2 = [i for i in dict1.keys() if len(dict1[i]) >= 2]
list3 = [i for i in dict1.keys()]
list1.sort(key = lambda x: dict2[x])
list2.sort(key = lambda x: dict2[x])
list3.sort(key = lambda x: dict2[x])
dict3 = {i:i for i in xrange(n+1)}
dict4 = {i:i for i in xrange(n)}
dict5 = {i:i for i in xrange(n+1)}

def parent(start, visited, graph):
    end = graph[start]
    if start == end:
        for num in visited:
            graph[num] = start
        return start

    visited.append(end)
    return parent(end, visited, graph)

count = 0
for i in list1:
    a = dict1[i][0]
    parent1 = parent(a, [a], dict3)
    parent2 = parent(n, [n], dict3)
    if parent1 != parent2:
        dict3[parent1] = parent2
        count += dict2[i]

for i in dict3:
    parent(i, [i], dict3)
    
ans = all(dict3[i] == dict3[0] for i in dict3)
if ans:
    count1 = count
else:
    count1 = 1e9
    
count = 0
for i in list2:
    a = dict1[i][0]
    b = dict1[i][1]
    parent1 = parent(a, [a], dict4)
    parent2 = parent(b, [b], dict4)
    if parent1 != parent2:
        dict4[parent1] = parent2
        count += dict2[i]

for i in dict4:
    parent(i, [i], dict4)
    
ans = all(dict4[i] == dict4[0] for i in dict4)
if ans:
    count2 = count
else:
    count2 = 1e9
    
count = 0
for i in list3:
    a = dict1[i][0]
    try:
        b = dict1[i][1]
        parent2 = parent(b, [b], dict5)
    except IndexError:
        parent2 = parent(n, [n], dict5)
    parent1 = parent(a, [a], dict5)
    
    if parent1 != parent2:
        dict5[parent1] = parent2
        count += dict2[i]

for i in dict5:
    parent(i, [i], dict5)
    
ans = all(dict5[i] == dict5[0] for i in dict5)
if ans:
    count3 = count
else:
    count3 = 1e9

print min(count1, count2, count3)
