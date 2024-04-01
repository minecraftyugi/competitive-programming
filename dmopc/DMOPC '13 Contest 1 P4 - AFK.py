import sys
raw_input = sys.stdin.readline

n = input()

def paths(starts, end, cost, graph, visited):
    new = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    if cost == 60:
        return "#notworth"
    
    for start in starts:
        for direction in directions:
            y, x = start
            yy, xx = direction
            newY, newX = y + yy, x + xx
            if 0 <= newY < w and 0 <= newX < l:
                if (newY, newX) == end:
                    return cost
                
                if graph[newY][newX] != "X" and ((newY,newX)) not in visited:
                    new.add((newY, newX))
                    visited.add((newY, newX))
            
    if len(new) == 0:
        return "#notworth"
    
    return paths(new, end, cost + 1, graph, visited)

for i in xrange(n):
    l, w = map(int, raw_input().split())
    grid = []
    
    for j in xrange(w):
        line = raw_input()
        grid.append(line)
        check1 = line.find("C")
        check2 = line.find("W")
        if check1 != -1:
            sy, sx = j, check1
        if check2 != -1:
            fy, fx = j, check2

    if abs(fy - sy) + abs(fx - sx) >= 60:
        print "#notworth"
        continue
    
    print paths([(sy, sx)], (fy, fx), 1, grid, set())
