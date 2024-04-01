import sys

raw_input = sys.stdin.readline
r = int(raw_input())
c = int(raw_input())
grid = []
starts = []
moves = []
results = []
directions = "UDLR"

for i in xrange(r):
    line = raw_input().strip()
    for index, value in enumerate(line):
        if value == ".":
            starts.append((i, index))
            
    grid.append(list(line))

m = int(raw_input())
for i in xrange(m):
    moves.append(raw_input().strip())

def valid(x, y):
    if x < 0 or x == r or y < 0 or y == c:
        return False

    if grid[x][y] == "X":
        return False
    
    return True

def paths(start, graph, direction):
    x, y = start
    for move in moves:
        if direction == "U":
            if move == "F":
                x -= 1
                if not valid(x, y):
                    return False
            elif move == "R":
                direction = "R"
            else:
                direction = "L"
        elif direction == "D":
            if move == "F":
                x += 1
                if not valid(x, y):
                    return False
            elif move == "R":
                direction = "L"
            else:
                direction = "R"
        elif direction == "L":
            if move == "F":
                y -= 1
                if not valid(x, y):
                    return False
            elif move == "R":
                direction = "U"
            else:
                direction = "D"
        else:
            if move == "F":
                y += 1
                if not valid(x, y):
                    return False
            elif move == "R":
                direction = "D"
            else:
                direction = "U"

    return (x, y)

for start in starts:
    for direction in directions:
        result = paths(start, grid, direction)
        if result:
            results.append(result)

for x, y in results:
    grid[x][y] = "*"

for line in grid:
    print "".join(line)
