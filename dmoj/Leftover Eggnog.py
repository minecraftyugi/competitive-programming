import sys
sys.setrecursionlimit(10000)
a, b, m = map(int, raw_input().split())

def path(starts, end, visited, parents):
    if len(starts) == 0:
        return "Not possible"
    new = set()
    for start in starts:
        cupA = start[0]
        cupB = start[1]
        if cupA == end or cupB == end:
            ans = []
            parent = parents[start][1]
            ans += [parents[start][0]]
            while parent != (0, 0):
                ans += [parents[parent][0]]
                parent = parents[parent][1]

            ans.reverse()
            return"\n".join(ans)
        
        #fill
        if (a, cupB) not in visited:
            visited.add((a, cupB))
            new.add((a, cupB))
            parents[(a, cupB)] = ("fill A",start)

        if (cupA, b) not in visited:
            visited.add((cupA, b))
            new.add((cupA, b))
            parents[(cupA, b)] = ("fill B",start)

        #pour
        diffA = a - cupA
        diffB = b - cupB
        if cupA > diffB:
            A = cupA - diffB
            B = b
            if (A, B) not in visited:
                visited.add((A, B))
                new.add((A, B))
                parents[(A, B)] = ("pour A B",start)
        else:
            A = 0
            B = cupB + cupA
            if (A, B) not in visited:
                visited.add((A, B))
                new.add((A, B))
                parents[(A, B)] = ("pour A B",start)

        if cupB > diffA:
            A = a
            B = cupB - diffA
            if (A, B) not in visited:
                visited.add((A, B))
                new.add((A, B))
                parents[(A, B)] = ("pour B A",start)
        else:
            A = cupA + cupB
            B = 0
            if (A, B) not in visited:
                visited.add((A, B))
                new.add((A, B))
                parents[(A, B)] = ("pour B A",start)

        #chug
        if (0, cupB) not in visited:
            visited.add((0, cupB))
            new.add((0, cupB))
            parents[(0, cupB)] = ("chug A",start)

        if (cupA, 0) not in visited:
            visited.add((cupA, 0))
            new.add((cupA, 0))
            parents[(cupA, 0)] = ("chug B",start)
            
    return path(new, end, visited, parents)

print path([(0, 0)], m, set(), {})
