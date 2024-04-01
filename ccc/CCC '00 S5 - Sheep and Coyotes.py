import math

n = input()
coords = [(0,0)]
dict1 = {}

for i in xrange(n):
    x = input()*1.0
    y = input()*1.0
    if x not in dict1:
        dict1[x] = y
        coords.append((x, y))
    else:
        if y < dict1[x]:
            coords.remove((x, dict1[x]))
            dict1[x] = y
            coords.append((x, y))

coords.sort()
coords.append((1000,0))

def dist(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def intersection(x1, y1, x2, y2):
    return (y2**2 - y1**2 + x2**2 - x1**2)/(2.0*(x2-x1))

while 1:
    check = True
    if len(coords) == 3:
        break
    
    for index, coord in enumerate(coords):
        x, y = coord
        if index == 0 or index == len(coords)-1:
            continue
        elif index == 1:
            x2, y2 = coords[index+1]
            if dist(x2, y2, x, 0) < y and dist(x2, y2, 0, 0) < dist(x, y, 0, 0):
                coords.pop(index)
                check = False
                break
        elif index == len(coords) - 2:
            x2, y2 = coords[index-1]
            if dist(x2, y2, x, 0) < y and dist(x2, y2, 1000, 0) < dist(x, y, 1000, 0):
                coords.pop(index)
                check = False
                break
        else:
            x2, y2 = coords[index+1]
            x3, y3 = coords[index-1]
            h = intersection(x, y, x2, y2)
            if dist(x2, y2, x, 0) < y and dist(x3, y3, h, 0) < dist(x, y, h, 0):
                coords.pop(index)
                check = False
                break
            
            h = intersection(x, y, x3, y3)
            if dist(x3, y3, x, 0) < y and dist(x2, y2, h, 0) < dist(x, y, h, 0):
                coords.pop(index)
                check = False
                break
        
    if check is True:
        break

for coord in coords[1:-1]:
    print "The sheep at ({:.2f}, {:.2f}) might be eaten.".format(coord[0], coord[1])
