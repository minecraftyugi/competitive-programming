x = input()
y = input()
lists = [[""for i in xrange(12)]for i in xrange(12)]
direction = "D"
posX, posY = 5, 6

if x > 9:
    lists[5][5] = str(x)
else:
    lists[5][5] = " " + str(x)


for i in xrange(x+1, y+1):
    if i > 9:
        lists[posY][posX] = str(i)
    else:
        lists[posY][posX] = " " + str(i)
        
    if direction == "D":
        if lists[posY][posX+1] == "":
            direction = "R"
            posX += 1
        else:
            posY += 1
    elif direction == "R":
        if lists[posY-1][posX] == "":
            direction = "U"
            posY -= 1
        else:
            posX += 1
    elif direction == "U":
        if lists[posY][posX-1] == "":
            direction = "L"
            posX -= 1
        else:
            posY -= 1
    else:
        if lists[posY+1][posX] == "":
            direction = "D"
            posY += 1
        else:
            posX -= 1

i = 0
maximum = 0
while i < len(lists):
    lists[i] = filter(None, lists[i])
    if not lists[i]:
        lists.pop(i)
    else:
        maximum = max(maximum, len(lists[i]))
        i += 1
    
if direction == "L":
    for i in xrange(maximum - len(lists[0])):
        lists[0].insert(0, "  ")
elif direction == "D":
    for i in xrange(len(lists)):
        if len(lists[i]) < maximum:
            lists[i].insert(0, "  ")

for i in lists:
    print " ".join(i)
