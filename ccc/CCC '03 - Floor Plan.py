amount = int(raw_input())
rows = int(raw_input())
columns = int(raw_input())
floor = []
rooms = []
dots = []
number = 0

def room(old, count):
    global dots
    new = []
    if old == []:
        return count
    for i in old:
        r, c, = i[0], i[1]
        if (r, c + 1) in dots:
            new.append((r, c + 1))
            dots.remove((r, c + 1))
            count += 1
        if (r, c - 1) in dots:
            new.append((r, c - 1))
            dots.remove((r, c - 1))
            count += 1
        if (r + 1, c) in dots:
            new.append((r + 1, c))
            dots.remove((r + 1, c))
            count += 1
        if (r - 1, c) in dots:
            new.append((r - 1, c))
            dots.remove((r - 1, c))
            count += 1

    return room(new, count)
    

for i in xrange(rows):
    floor.append(raw_input())

for i in xrange(rows):
    for j in xrange(columns):
        if floor[i][j] == ".":
            dots.append((i,j))

while 1:
    if dots == []:
        break
    start = [dots[0]]
    dots.pop(0)
    count = room(start, 1)
    rooms.append(count)

rooms = sorted(rooms, reverse=True)

for i in rooms:
    if amount - i >= 0:
        amount -= i
        number += 1
    else:
        break
if number != 1:
    print str(number) + " rooms, " + str(amount) + " square metre(s) left over"
else:
    print str(number) + " room, " + str(amount) + " square metre(s) left over"
