def finder(x, y):
    if x < 4:
        if y < 4: return 0
        elif y < 8: return 4
        elif y < 12: return 8
        else: return 12
    elif x < 8:
        if y < 4: return 1
        elif y < 8: return 5
        elif y < 12: return 9
        else: return 13
    elif x < 12:
        if y < 4: return 2
        elif y < 8: return 6
        elif y < 12: return 10
        else: return 14
    else:
        if y < 4: return 3
        elif y < 8: return 7
        elif y < 12: return 11
        else: return 15

for a in xrange(10):
    rows = [set()for i in xrange(16)]
    columns = [set()for i in xrange(16)]
    quad = [set()for i in xrange(16)]
    board = []
    count = 0
    
    for i in xrange(16):
        line = raw_input()
        board.append(line)
        for j in xrange(16):
            num = line[j]
            if num != "-":
                rows[i].add(num)
                columns[j].add(num)
                quadrant = finder(j, i)
                quad[quadrant].add(num)

    for y in xrange(16):
        for x in xrange(16):
            if board[y][x] == "-":
                quadrant = finder(x, y)
                for i in xrange(16):
                    i = hex(i)[2:].upper()
                    if i not in rows[y]|columns[x]|quad[quadrant]:
                        count += 1
                        rows[y].add(i)
                        columns[x].add(i)
                        quad[quadrant].add(i)
                        break

    print count
