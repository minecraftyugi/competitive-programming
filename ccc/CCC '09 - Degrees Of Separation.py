dict1 = { 1 : [6],
         2 : [6],
         3 : [4 , 5, 6, 15],
         4 : [3, 5, 6],
         5 : [3, 4, 6],
         6 : [1, 2, 3, 4, 5, 7],
         7 : [6, 8],
         8 : [7, 9],
         9 : [8, 10, 12],
         10 : [9, 11],
         11 : [10, 12],
         12 : [9, 13],
         13 : [12, 14, 15],
         14 : [13],
         15 : [3, 13],
         16 : [17, 18],
         17 : [16, 18],
         18 : [16, 17]
        }

shortest = 0

def find_shortest_path(graph, start, end, path=[]):
    global shortest
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

ltr = ""

while ltr != "q":
    ltr = raw_input()
    shortest = 0
    if ltr == "q":
        break
    if ltr == "i":
        x = int(raw_input())
        y = int(raw_input())
        if x in dict1 and y not in dict1:
            list1 = dict1[x]
            list1.append(y)
            list1.sort()
            dict2 = {x : list1}
            dict1.update(dict2)
            dict2 = {y : [x]}
            dict1.update(dict2)
        if y in dict1 and x not in dict1:
            list1 = dict1[y]
            list1.append(x)
            list1.sort()
            dict2 = {y : list1}
            dict1.update(dict2)
            dict2 = {x : [y]}
            dict1.update(dict2)
        if x not in dict1 and y not in dict1:
            dict2 = {x : [y]}
            dict1.update(dict2)
            dict2 = {y : [x]}
            dict1.update(dict2)
        if x not in dict1[y] and y not in dict1[x]:
            list1 = dict1[x]
            list1.append(y)
            list1.sort()
            dict2 = {x : list1}
            dict1.update(dict2)
            list1 = dict1[y]
            list1.append(x)
            list1.sort()
            dict2 = {y : list1}
            dict1.update(dict2)
    if ltr == "d":
        x = int(raw_input())
        y = int(raw_input())
        list1 = dict1[x]
        list1.remove(y)
    if ltr == "n":
        x = int(raw_input())
        if x not in dict1:
            print 0
        else:
            list1 = dict1[x]
            print len(list1)
    if ltr == "f":
        x = int(raw_input())
        if x not in dict1:
            print 0
            continue
        list1 = dict1[x]
        edges = []
        edgesNew = []
        for i in list1:
            for h in dict1[i]:
                edges.append([i, h])
        for i in xrange(len(edges)):
            if x not in edges[i] or dict1[x] == []:
                if edges[i][0] not in dict1[x] and edges[i][1] in dict1[x]:
                    edgesNew.append(edges[i])
                    continue
                if edges[i][0] in dict1[x] and edges[i][1] not in dict1[x]:
                    edgesNew.append(edges[i])
                    continue                
        print len(edgesNew)
    if ltr == "s":
        x = int(raw_input())
        y = int(raw_input())
        if x not in dict1 or y not in dict1:
            print "Not connected"
            continue 
        print len(find_shortest_path(dict1, x, y, path=[])) - 1

"""
    i x y - make person x and person y friends. If they are already friends, no change needs to be made. If either x or y is a new person, add them.
    d x y - delete the friendship between person x and person y.
    n x - output the number of friends that person x has.
    f x - output the number of "friends of friends" that person x has. Notice that x and direct friends of x are not counted as "friends of friends."
    s x y - output the degree of separation between x and y. If there is no path from x to y, output "Not connected".
    q - quit the program.
"""
