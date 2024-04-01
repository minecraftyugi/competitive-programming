import sys
sys.setrecursionlimit(100000)
raw_input = sys.stdin.readline

n, h = map(int, raw_input().split())
grid = [[0 for i in xrange(n)]for i in xrange(n)]

for i in xrange(n):
    line = map(int, raw_input().split())
    for index, value in enumerate(line):
        grid[i][index] = value

def path(starts, graph, visited):
    new = set()
    possible = [(0,1), (1,0), (0,-1), (-1,0)]
    
    for start in starts:
        x, y = start
        for move in possible:
            X, Y = move
            newX = x + X
            newY = y + Y
            if n > newX >= 0 and n > newY >= 0:
                if abs(grid[x][y] - grid[newX][newY]) <= h and (newX, newY) not in visited:
                    new.add((newX, newY))
                    visited.add((newX, newY))
                    if (newX, newY) == (n-1, n-1):
                        return "yes"

    if len(new) == 0:
        return "no"

    return path(new, graph, visited)

print path([(0,0)], grid, set())
