import sys
sys.setrecursionlimit(40)
def switch(starts, visited):
    new = set()

    for start in starts:
        if all([start[i][j] == "." for i in xrange(r) for j in xrange(c)]):
            return "S"
        for i in xrange(r):
            for j in xrange(c-3):
                newGrid = list(start)
                group = start[i][j:j+4]
                if group == ("X", "X", "O", "X"):
                    newGroup = tuple([".", ".", ".", "O"]+list(start[i][j+4:]))
                    newGrid[i] = newGroup
                    newGrid = tuple(newGrid)
                    new.add(newGrid)
                    visited.add(newGrid)
                elif group == ("X", "O", "X", "X"):
                    newGroup = tuple(["O", ".", ".", "."]+list(start[i][j+4:]))
                    newGrid[i] = newGroup
                    newGrid = tuple(newGrid)
                    new.add(newGrid)
                    visited.add(newGrid)
                elif group == ("O", "O", "X", "O"):
                    newGroup = tuple([".", ".", ".", "X"]+list(start[i][j+4:]))
                    newGrid[i] = newGroup
                    newGrid = tuple(newGrid)
                    new.add(newGrid)
                    visited.add(newGrid)
                elif group == ("O", "X", "O", "O"):
                    newGroup = tuple(["X", ".", ".", "."]+list(start[i][j+4:]))
                    newGrid[i] = newGroup
                    newGrid = tuple(newGrid)
                    new.add(newGrid)
                    visited.add(newGrid)
                else:
                    pass

        for i in xrange(c):
            for j in xrange(r-3):
                newGrid = list(start)
                group = tuple([start[k][i] for k in xrange(j, j+4)])
                if group == ("X", "X", "O", "X"):
                    newGrid[j] = tuple(list(newGrid[j][:i])+["."]+list(newGrid[j][i+1:]))
                    newGrid[j+1] = tuple(list(newGrid[j+1][:i])+["."]+list(newGrid[j+1][i+1:]))
                    newGrid[j+2] = tuple(list(newGrid[j+2][:i])+["."]+list(newGrid[j+2][i+1:]))
                    newGrid[j+3] = tuple(list(newGrid[j+3][:i])+["O"]+list(newGrid[j+3][i+1:]))
                    newGrid = tuple(newGrid)
                    new.add(newGrid)
                    visited.add(newGrid)
                elif group == ("X", "O", "X", "X"):
                    newGrid[j] = tuple(list(newGrid[j][:i])+["O"]+list(newGrid[j][i+1:]))
                    newGrid[j+1] = tuple(list(newGrid[j+1][:i])+["."]+list(newGrid[j+1][i+1:]))
                    newGrid[j+2] = tuple(list(newGrid[j+2][:i])+["."]+list(newGrid[j+2][i+1:]))
                    newGrid[j+3] = tuple(list(newGrid[j+3][:i])+["."]+list(newGrid[j+3][i+1:]))
                    newGrid = tuple(newGrid)
                    new.add(newGrid)
                    visited.add(newGrid)
                elif group == ("O", "O", "X", "O"):
                    newGrid[j] = tuple(list(newGrid[j][:i])+["."]+list(newGrid[j][i+1:]))
                    newGrid[j+1] = tuple(list(newGrid[j+1][:i])+["."]+list(newGrid[j+1][i+1:]))
                    newGrid[j+2] = tuple(list(newGrid[j+2][:i])+["."]+list(newGrid[j+2][i+1:]))
                    newGrid[j+3] = tuple(list(newGrid[j+3][:i])+["X"]+list(newGrid[j+3][i+1:]))
                    newGrid = tuple(newGrid)
                    new.add(newGrid)
                    visited.add(newGrid)
                elif group == ("O", "X", "O", "O"):
                    newGrid[j] = tuple(list(newGrid[j][:i])+["O"]+list(newGrid[j][i+1:]))
                    newGrid[j+1] = tuple(list(newGrid[j+1][:i])+["."]+list(newGrid[j+1][i+1:]))
                    newGrid[j+2] = tuple(list(newGrid[j+2][:i])+["."]+list(newGrid[j+2][i+1:]))
                    newGrid[j+3] = tuple(list(newGrid[j+3][:i])+["."]+list(newGrid[j+3][i+1:]))
                    newGrid = tuple(newGrid)
                    new.add(newGrid)
                    visited.add(newGrid)
                else:
                    pass
                
    if len(new) == 0:
        return "N"
    
    return switch(new, visited)

for i in xrange(1):
    r, c = map(int, raw_input().split())
    ans = ""
    for i in xrange(5):
        grid = []
        for i in xrange(r):
            grid.append(tuple(raw_input()))

        grid = tuple(grid)
        print switch([grid], set())
