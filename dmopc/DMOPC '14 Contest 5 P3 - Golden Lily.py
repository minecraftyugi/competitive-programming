l, d = map(int, raw_input().split())
graph = [[0 for i in xrange(l)] for i in xrange(d)]
grid = []

for i in xrange(d):
    line = map(int, raw_input().split())
    grid.append(line)

x, y = map(int, raw_input().split())

for i in xrange(d):
    for j in xrange(l):
        if i == 0:
            if j == 0:
                graph[i][j] = grid[i][j]
            else:
                graph[i][j] = graph[i][j-1] + grid[i][j]
        else:
            if j == 0:
                graph[i][j] = graph[i-1][j] + grid[i][j]
            else:
                graph[i][j] = min(graph[i-1][j], graph[i][j-1]) + grid[i][j]

    for j in xrange(l):
        if j != l - 1:
            graph[i][j] = min(graph[i][j], graph[i][j+1] + grid[i][j])


print graph[y][x]
