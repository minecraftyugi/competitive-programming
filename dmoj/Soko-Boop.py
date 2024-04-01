import sys
sys.setrecursionlimit(100000)
r, c = map(int, raw_input().split())
dict1 = {}

for i in xrange(r):
    line = list(raw_input())
    for j, char in enumerate(line):
        if char == "P":
            start = (i, j)
            dict1[(i,j)] = "."
        elif char == "B":
            box = (i, j)
            dict1[(i,j)] = "."
        elif char == "X":
            end = (i, j)
            dict1[(i,j)] = "."
        elif char == ".":
            dict1[(i,j)] = "."
        else:
            dict1[(i,j)] = "#"

try:
    start, box, end
except NameError:
    print -1
    sys.exit()
    
def path(starts, last, moves, graph, visited):
    new = set()

    if len(starts) == 0:
        return -1
    
    for player, boxPos in starts:
        if boxPos == last:
            return moves

        x, y = player
        a, b = boxPos
        if (x+1, y) == (a,b):
            try:
                if ((x+1, y), (a+1,b)) not in visited and graph[(a+1,b)]==".":
                    visited.add(((x+1, y), (a+1,b)))
                    new.add(((x+1, y), (a+1,b)))
            except KeyError:
                pass
        else:
            try:
                if ((x+1, y), (a,b)) not in visited and graph[(x+1,y)]==".":
                    visited.add(((x+1, y), (a,b)))
                    new.add(((x+1, y), (a,b)))
            except KeyError:
                pass

        if (x-1, y) == (a,b):
            try:
                if ((x-1, y), (a-1,b)) not in visited and graph[(a-1,b)]==".":
                    visited.add(((x-1, y), (a-1,b)))
                    new.add(((x-1, y), (a-1,b)))
            except KeyError:
                pass
        else:
            try:
                if ((x-1, y), (a,b)) not in visited and graph[(x-1,y)]==".":
                    visited.add(((x-1, y), (a,b)))
                    new.add(((x-1, y), (a,b)))
            except KeyError:
                pass

        if (x, y+1) == (a,b):
            try:
                if ((x, y+1), (a,b+1)) not in visited and graph[(a,b+1)]==".":
                    visited.add(((x, y+1), (a,b+1)))
                    new.add(((x, y+1), (a,b+1)))
            except KeyError:
                pass
        else:
            try:
                if ((x, y+1), (a,b)) not in visited and graph[(x,y+1)]==".":
                    visited.add(((x, y+1), (a,b)))
                    new.add(((x, y+1), (a,b)))
            except KeyError:
                pass

        if (x, y-1) == (a,b):
            try:
                if ((x, y-1), (a,b-1)) not in visited and graph[(a,b-1)]==".":
                    visited.add(((x, y-1), (a,b-1)))
                    new.add(((x, y-1), (a,b-1)))
            except KeyError:
                pass
        else:
            try:
                if ((x, y-1), (a,b)) not in visited and graph[(x,y-1)]==".":
                    visited.add(((x, y-1), (a,b)))
                    new.add(((x, y-1), (a,b)))
            except KeyError:
                pass
        
    return path(new, last, moves+1, graph, visited)

print path([(start, box)], end, 0, dict1, set())
