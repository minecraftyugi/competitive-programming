width = input()
height = input()
w = input()
h = input()
steps = input()
grid = [[0]*width for i in xrange(height)]

for i in xrange(height):
    for j in xrange(width):
        if ((i < h or height - 1 - i < h) and j < w) or \
           ((i < h or height - 1 - i < h) and width - 1 - j < w):
            grid[i][j] = 1

def blocked(r, c):
    return (r < 0 or r == height or c < 0 or c == width or grid[r][c])

pos = (0, w)
move = "R"
for i in xrange(steps):
    grid[pos[0]][pos[1]] = 1
    if move == "R":
        if blocked(pos[0]-1, pos[1]):
            if blocked(pos[0], pos[1]+1):
                move = "D"
                if blocked(pos[0]+1, pos[1]):
                    break
                else:
                    pos = (pos[0]+1, pos[1])
            else:
                pos = (pos[0], pos[1]+1)
        else:
            move = "U"
            pos = (pos[0]-1, pos[1])
    elif move == "D":
        if blocked(pos[0], pos[1]+1):
            if blocked(pos[0]+1, pos[1]):
                move = "L"
                if blocked(pos[0], pos[1]-1):
                    break
                else:
                    pos = (pos[0], pos[1]-1)
            else:
                pos = (pos[0]+1, pos[1])
        else:
            move = "R"
            pos = (pos[0], pos[1]+1)
    elif move == "L":
        if blocked(pos[0]+1, pos[1]):
            if blocked(pos[0], pos[1]-1):
                move = "U"
                if blocked(pos[0]-1, pos[1]):
                    break
                else:
                    pos = (pos[0]-1, pos[1])
            else:
                pos = (pos[0], pos[1]-1)
        else:
            move = "D"
            pos = (pos[0]+1, pos[1])
    else:
        if blocked(pos[0], pos[1]-1):
            if blocked(pos[0]-1, pos[1]):
                move = "R"
                if blocked(pos[0], pos[1]+1):
                    break
                else:
                    pos = (pos[0], pos[1]+1)
            else:
                pos = (pos[0]-1, pos[1])
        else:
            move = "L"
            pos = (pos[0], pos[1]-1)

print pos[1] + 1
print pos[0] + 1
