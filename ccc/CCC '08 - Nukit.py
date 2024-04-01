n = input()

def moves(starts, count, parents, visited, graph):
    new = set()
    possible = [(-2,-1,0,-2),(-1,-1,-1,-1),(0,0,-2,-2),(0,-3,0,0),(-1,0,0,-1)]

    if len(starts) == 0:
        dict1 = {}
        points = [thing]
        visit = set()
        ans = []
        while 1:
            if len(points) == 0:
                break

            newSet = set()
            for point in points:
                neighbours = graph[point]
                if neighbours == []:
                    ans.add(point)
                    
                for neighbour in neighbours:
                    newSet.add(neighbour)

    for thing1 in starts:
        A, B, C, D = thing1
        graph[thing1] = []
        for thing2 in possible:
            a, b, c, d = thing2
            newMoves = (A+a, B+b, C+c, D+d)
            if all(newMoves) >= 0 and newMoves not in visited:
                visited.add(newMoves)
                new.add(newMoves)
                graph[thing1] += [newMoves]
                if count % 2 == 0:
                    parents[newMoves] = (thing1, "Patrick")
                else:
                    parents[newMoves] = (thing1, "Roland")
    
    for A, B, C, D in starts:
        check = 0
        if A >= 2 and B >= 1 and D >= 2:
            if (A-2,B-1,C,D-2) not in visited:
                check = 1
                visited.add((A-2,B-1,C,D-2))
                new.add((A-2,B-1,C,D-2))
                if count % 2 == 0:
                    parents[(A-2,B-1,C,D-2)] = ((A,B,C,D), "Patrick")
                else:
                    parents[(A-2,B-1,C,D-2)] = ((A,B,C,D), "Roland")

        if A >= 1 and B >= 1 and C >= 1 and D >= 1:
            if (A-1,B-1,C-1,D-1) not in visited:
                check = 1
                visited.add((A-1,B-1,C-1,D-1))
                new.add((A-1,B-1,C-1,D-1))
                if count % 2 == 0:
                    parents[(A-1,B-1,C-1,D-1)] = ((A,B,C,D), "Patrick")
                else:
                    parents[(A-1,B-1,C-1,D-1)] = ((A,B,C,D), "Roland")

        if C >= 2 and D >= 1:
            if (C,D-2) not in visited:
                check = 1
                visited.add((C,D-2))
                new.add((C,D-2))
                if count % 2 == 0:
                    parents[(C,D-2)] = ((A,B,C,D), "Patrick")
                else:
                    parents[(C,D-2)] = ((A,B,C,D), "Roland")

        if B >= 3:
            if (B-3) not in visited:
                check = 1
                visited.add((B-3))
                new.add((B-3))
                if count % 2 == 0:
                    parents[(B-3)] = ((A,B,C,D), "Patrick")
                else:
                    parents[(B-3)] = ((A,B,C,D), "Roland")

        if A >= 1 and D >= 1:
            if (A-1,D-1) not in visited:
                check = 1
                visited.add((A-1,D-1))
                new.add((A-1,D-1))
                if count % 2 == 0:
                    parents[(A-1,D-1)] = ((A,B,C,D), "Patrick")
                else:
                    parents[(A-1,D-1)] = ((A,B,C,D), "Roland")
                    
    return moves(new, count + 1, parents, visited, graph)

for i in xrange(n):
    first = map(int, raw_input().split())
    a, b, c, d = first
