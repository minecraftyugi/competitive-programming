lines = raw_input().split()

rows = int(lines[0])
columns = int(lines[1])
lineList = []
dotList = []
count = 0

def maze(nodes=[]):
    global dotList
    newnodes = []

    if nodes == []:
        return
    
    for node in nodes:
        dotList.pop(dotList.index(node))
        x = node[0]
        y = node[1]

        if x > 0:
            if lineList[x-1][y] == "." and (x-1, y) in dotList:
                newnodes += [(x-1, y)]
        if x < rows - 1:
            if lineList[x+1][y] == "." and (x+1, y) in dotList:
                newnodes += [(x+1, y)]
        if y > 0:
            if lineList[x][y-1] == "." and (x, y-1) in dotList:
                newnodes += [(x, y-1)]
        if y < columns - 1:
            if lineList[x][y+1] == "." and (x, y+1) in dotList:
                newnodes += [(x, y+1)]

    nodes = []        
    nodes += set(newnodes)
    maze(nodes)
    return

for i in range(rows):
    line = raw_input()
    lineList.append(line)

    for j in range(columns):
        if line[j] == ".":
            dotList.append((i,j))

while dotList != []:
    maze([dotList[0]])
    count += 1

print count
