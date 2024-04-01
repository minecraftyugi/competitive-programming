r, c = map(int, raw_input().split())
sy, sx = map(int, raw_input().split())
fy, fx = map(int, raw_input().split())
grid = []

for i in xrange(r):
    line = list(raw_input())
    grid.append(line)

t = input()

for i in xrange(t):
    y, x = map(int, raw_input().split())
    grid[y][x] = "."


def paths(starts, end, cost, graph, visited):
    new = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for start in starts:
        for direction in directions:
            y, x = start
            yy, xx = direction
            newY, newX = y + yy, x + xx
            if 0 <= newY < r and 0 <= newX < c and (newY, newX) not in visited:
                if graph[newY][newX] != "X":
                    if (newY, newX) == end:
                        return cost
                    else:
                        new.add((newY, newX))
                        visited.add((newY, newX))
        
    return paths(new, end, cost + 1, graph, visited)

def paths2(starts, cost, graph, visited):
    new = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for start in starts:
        for direction in directions:
            y, x = start
            yy, xx = direction
            newY, newX = y + yy, x + xx
            if 0 <= newY < r and 0 <= newX < c and (newY, newX) not in visited:
                if graph[newY][newX] == ".":
                        return cost
                if graph[newY][newX] != "X":
                    new.add((newY, newX))
                    visited.add((newY, newX))                
        
    return paths2(new, cost + 1, graph, visited)

longer = paths([(sy, sx)], (fy, fx), 1, grid, set())
shorter = paths2([(sy, sx)], 1, grid, set())

print longer - shorter if grid[sy][sx] != "." else longer
