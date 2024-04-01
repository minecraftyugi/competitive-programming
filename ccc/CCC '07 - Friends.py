import sys
sys.setrecursionlimit(100000)
raw_input = sys.stdin.readline
n = int(raw_input())
dict1 = {}

for i in xrange(n):
    friends = map(int, raw_input().split())
    x = friends[0]
    y = friends[1]
    dict1[x] = y

def paths(start, end, graph, graph2, count):
    try:
        start = graph[start]
    except KeyError:
        return "No"
    count += 1
    if start == end:
        return "Yes " + str(count)
    try:
        check = graph2[start]
        return "No"
    except KeyError:
        graph2[start] = 1
        return paths(start, end, graph, graph2, count)

while 1:
    people = map(int, raw_input().split())
    x = people[0]
    y = people[1]
    if x == 0 and y == 0:
        break
    print paths(x, y, dict1, {x : 1}, -1)
