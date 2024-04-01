import sys
sys.setrecursionlimit(100000)
n,m = map(int, raw_input().split())
dict1 = {}
dict2 = {}
count = 0

for j in range(n,0,-1):
    line = raw_input()
    for i in range(1, m+1):
        dict1[(i,j)] = line[i-1]
        dict2[(i,j)] = {i:i for i in xrange(1,5)}

def paths(start1, start2, direction, graph, visited, backup):
    try:
        print count, start1, start2, graph[start2], direction
    except:
        print direction, "ERROR"
    if start2 == start1:
        for group in visited:
            point = group[0]
            direction = group[1]
            if direction == (1,0):
                direction = 1
            if direction == (0, 1):
                direction = 2
            if direction == (-1, 0):
                direction = 3
            if direction == (0, -1):
                direction = 4
            backup[point][direction] = start1
        return 1
    
    x,y = start2[0], start2[1]
    
    if x<1 or y<1 or x>m or y>n:
        if direction == (1,0):
                x -= 1
        if direction == (0, 1):
            y -= 1
        if direction == (-1, 0):
            x += 1
        if direction == (0, -1):
            y += 1
                
        for group in visited:
            point = group[0]
            direction = group[1]
            if direction == (1,0):
                direction = 1
            if direction == (0, 1):
                direction = 2
            if direction == (-1, 0):
                direction = 3
            if direction == (0, -1):
                direction = 4

            backup[point][direction] = "ERROR"
        return 0
    
    visited.append([(x,y),direction])
    
    if graph[start2] == "*":
        return 0
    if graph[start2] == "X":
        if direction == (0, 1):
            direction = (0, -1)
            return paths(start1, (x, y-1), (0, -1), graph, visited, backup)
        if direction == (1, 0):
            direction = (-1, 0)
            return paths(start1, (x-1, y), (-1, 0), graph, visited, backup)
        if direction == (0, -1):
            direction = (0, 1)
            return paths(start1, (x, y+1), (0, 1), graph, visited, backup)
        if direction == (-1, 0):
            direction = (1, 0)
            return paths(start1, (x+1, y), (1, 0), graph, visited, backup)

    if graph[start2] == "/":
        if direction == (0, 1):
            direction = (1, 0)
            return paths(start1, (x+1, y), (1, 0), graph, visited, backup)
        if direction == (1, 0):
            direction = (0, 1)
            return paths(start1, (x, y+1), (0, 1), graph,visited, backup)
        if direction == (0, -1):
            direction = (-1, 0)
            return paths(start1, (x-1, y), (-1, 0), graph,visited, backup)
        if direction == (-1, 0):
            direction = (0, -1)
            return paths(start1, (x, y-1), (0, -1), graph,visited, backup)

    if graph[start2] == "\\":
        if direction == (0, 1):
            direction = (-1, 0)
            return paths(start1, (x-1, y), (-1, 0), graph,visited, backup)
        if direction == (1, 0):
            direction = (0, -1)
            return paths(start1, (x, y-1), (0, -1), graph,visited, backup)
        if direction == (0, -1):
            direction = (1, 0)
            return paths(start1, (x+1, y), (1, 0), graph,visited, backup)
        if direction == (-1, 0):
            direction = (0, 1)
            return paths(start1, (x, y+1), (0, 1), graph,visited, backup)

    if graph[start2] == ".":
            if direction == (0, 1):
                return paths(start1, (x, y+1), (0, 1), graph,visited, backup)
            if direction == (1, 0):
                return paths(start1, (x+1, y), (1, 0), graph,visited, backup)
            if direction == (0, -1):
                return paths(start1, (x, y-1), (0, -1), graph,visited, backup)
            if direction == (-1, 0):
                return paths(start1, (x-1, y), (-1, 0), graph,visited, backup)

for point in dict1:
    if dict1[point] == ".":    
        x = point[0]
        y = point[1]
        ans = 0

        if dict2[point][2] == "ERROR":
            print point, (0,1), "Not valid"
            pass
        elif dict2[point][2] != 2:
            x = dict2[point][2][0]
            y = dict2[point][2][1]
            ans += paths(dict2[point][2], (x, y+1), (0, 1), dict1, [[(x,y),(0,1)]], dict2)
        else:
            ans += paths(point, (x, y+1), (0, 1), dict1, [[(x,y),(0,1)]], dict2)
        if ans >0:
            count +=1
            continue
        
        if dict2[point][1] == "ERROR":
            print point, (1,0), "Not valid"
            pass
        elif dict2[point][1] != 1:
            x = dict2[point][1][0]
            y = dict2[point][1][1]
            ans += paths(dict2[point][1], (x+1, y), (1, 0), dict1, [[(x,y),(1,0)]], dict2)
        else:
            ans += paths(point, (x+1, y), (1, 0), dict1, [[(x,y),(1,0)]], dict2)
        if ans >0:
            count +=1
            continue

        if dict2[point][4] == "ERROR":
            print point, (0,-1), "Not valid"
            pass
        elif dict2[point][4] != 4:
            x = dict2[point][4][0]
            y = dict2[point][4][1]
            ans += paths(dict2[point][4], (x, y-1), (0, -1), dict1, [[(x,y),(0,-1)]], dict2)
        else:
            ans += paths(point, (x, y-1), (0, -1), dict1, [[(x,y),(0,-1)]], dict2)
        if ans >0:
            count +=1
            continue
        
        if dict2[point][3] == "ERROR":
            print point, (-1,0), "Not valid"
            pass
        elif dict2[point][3] != 3:
            x = dict2[point][3][0]
            y = dict2[point][3][1]
            ans += paths(dict2[point][3], (x-1, y), (-1, 0), dict1, [[(x,y),(-1,0)]], dict2)
        else:
            ans += paths(point, (x-1, y), (-1, 0), dict1, [[(x,y),(-1,0)]], dict2)
        if ans >0:
            count +=1
            continue
        
print count

"""
5 6
/.\...
./.\.X
\.....
/\./X*
\/.*\.
"""
