c, n = map(int, raw_input().split())
food = map(int, raw_input().split())
food.sort()
calories = [0]*c
indexes = [0]
for f in food:
    add = []
    for index in indexes:
        pos = f + index
        if pos < c and not calories[pos]:
            calories[pos] = 1
            add.append(pos)

    indexes.extend(add)

found = False
index = c-1
while index and not found:
    if calories[index]:
        print index
        found = True

    index -= 1

if not found:
    print 0
