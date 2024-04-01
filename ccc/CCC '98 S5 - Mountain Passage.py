import sys, heapq

raw_input = sys.stdin.readline
n = int(raw_input())
def valid(x, y, size):
    return 0 <= x < size and 0 <= y < size

def shortest(g, dist, visited, size, h):
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    heap = [(0, (0, 0))]
    start = (0, 0)
    cost = 0
    found = True
    while heap or found:
        for x, y in directions:
            newx, newy = start[0]+x, start[1]+y
            if valid(newx, newy, size):
                c = cost + (g[newx][newy] > h or g[start[0]][start[1]] > h)
                gap = abs(g[start[0]][start[1]] - g[newx][newy])
                if c < dist[newx][newy] and gap <= 2:
                    dist[newx][newy] = c
                    heapq.heappush(heap, (c, (newx, newy)))

        found = False
        while heap and not found:
            cost, start = heapq.heappop(heap)
            if not visited[start[0]][start[1]]:
                visited[start[0]][start[1]] = 1
                found = True

    if not visited[size-1][size-1]:
        return "CANNOT MAKE THE TRIP"
    
    return dist[size-1][size-1]

for i in xrange(n):
    m = int(raw_input())
    grid = [[0]*m for _ in xrange(m)]
    dist = [[1000]*m for _ in xrange(m)]
    dist[0][0] = 0
    visited = [[0]*m for _ in xrange(m)]
    visited[0][0] = 1
    for x in xrange(m):
        for y in xrange(m):
            grid[x][y] = int(raw_input())

    height = grid[0][0]
    print shortest(grid, dist, visited, m, height)
