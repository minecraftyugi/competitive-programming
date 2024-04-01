grid = {(i, j):0 for i in range(10) for j in range(9)}
G = {(i, j):[] for i in range(10) for j in range(9)}

def convert(coord):
    x = ord(coord[0]) - ord("A")
    y = int(coord[1]) - 1
    return (x, y)

for i in range(10):
    line = raw_input().split()
    for j in range(9):
        if not line[j].isdigit():
            coords = line[j].split("+")
            coords = map(convert, coords)
            G[(i, j)] = coords
        else:
            grid[(i, j)] = int(line[j])

visited = {(i, j):0 for i in range(10) for j in range(9)}
def explore(node):
    if visited[node] == 1:
        return -1
    elif visited[node] == 2:
        return grid[node]
    
    visited[node] = 1
    count = grid[node]
    for neighbour in G[node]:
        num = explore(neighbour)
        if num == -1:
            return -1
        else:
            count += num
            
    visited[node] = 2
    grid[node] = count
    return count

for i in range(10):
    s = []
    for j in range(9):
        val = explore((i, j))
        if val == -1:
            s.append("*")
        else:
            s.append(str(val))

    print " ".join(s)
