import sys, heapq

raw_input = sys.stdin.readline
n, s = map(int, raw_input().split())
distances = map(int, raw_input().split())
heaps = [[]for i in xrange(100)]
remove = [{}for i in xrange(100)]
stores = [set()for i in xrange(100000)]
time = 0
for i in xrange(s):
    stand, a = map(int, raw_input().split())
    ID = stand - 1
    stores[ID].update({a})
    heapq.heappush(heaps[a], (distances[ID], ID, time))

q = input()
for i in xrange(q):
    l = raw_input().split()
    query = l[0]
    time += 1
    if query == "A":
        ID, a = int(l[1]) - 1, int(l[2])
        stores[ID].update({a})
        heapq.heappush(heaps[a], (distances[ID], ID, time))
    elif query == "S":
        ID, a = int(l[1]) - 1, int(l[2])
        if a in stores[ID]:
            stores[ID].remove(a)
            remove[a][ID] = time
    elif query == "E":
        ID, dist = int(l[1]) - 1, int(l[2])
        for apple in stores[ID]:
            remove[apple][ID] = time
        
        distances[ID] = dist
    else:
        a = int(l[1])
        found = False
        try:
            while heaps[a] and not found:
                dist, ID, t = heaps[a][0]
                if t < remove[a].get(ID, 0):
                    heapq.heappop(heaps[a])
                else:
                    found = True
        except IndexError:
            pass

        if found:
            print ID + 1
        else:
            print -1
