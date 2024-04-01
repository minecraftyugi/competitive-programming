line = ""
dig = [[0, -1], [0, -2], [0, -3], [1, -3], [2, -3], [3, -3], [3, -4],
       [3, -5], [4, -5], [5, -5], [5, -4], [5, -3], [6, -3], [7, -3],
       [7, -4], [7, -5], [7, -6], [7, -7], [6, -7], [5, -7], [4, -7],
       [3, -7], [2, -7], [1, -7], [0, -7], [-1, -7], [-1, -6], [-1, -5]]

while line != "q":
    line = raw_input()
    line = line.split(" ")
    state = "safe"
    if line[0] == "q":
        break
    if line[0] == "r":
        for i in xrange(int(line[1])):
            digIndex = dig[len(dig) - 1]
            digX = digIndex[0]
            digY = digIndex[1]
            coord = [digX + 1, digY]
            if coord in dig:
                state = "DANGER"
            dig.append(coord)
    if line[0] == "l":
        for i in xrange(int(line[1])):
            digIndex = dig[len(dig) - 1]
            digX = digIndex[0]
            digY = digIndex[1]
            coord = [digX - 1, digY]
            if coord in dig:
                state = "DANGER"
            dig.append(coord)
    if line[0] == "d":
        for i in xrange(int(line[1])):
            digIndex = dig[len(dig) - 1]
            digX = digIndex[0]
            digY = digIndex[1]
            coord = [digX, digY - 1]
            if coord in dig:
                state = "DANGER"
            dig.append(coord)
    if line[0] == "u":
        for i in xrange(int(line[1])):
            digIndex = dig[len(dig) - 1]
            digX = digIndex[0]
            digY = digIndex[1]
            coord = [digX, digY + 1]
            if coord in dig:
                state = "DANGER"
            dig.append(coord)
    print str(coord[0])+" "+str(coord[1])+" "+state
    if state == "DANGER":
        break
    else:
        continue
