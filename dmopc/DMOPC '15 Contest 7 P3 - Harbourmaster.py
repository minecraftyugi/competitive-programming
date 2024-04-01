import itertools
c, s, p = map(float, raw_input().split())
n = input()
trait1 = 0
trait2 = 0
trait3 = 0
traits = []
minimum = 0

if n <= 5:
    for i in xrange(n):
        x, y, z = map(int, raw_input().split())
        trait1 += x
        trait2 += y
        trait3 += z

    lists = [trait1/c*100, trait2/s*100, trait3/p*100]
    
    if min(lists) >= 100:
        print 100.0
    else:
        print round(min(lists), 1)
else:
    for i in xrange(n):
        x, y, z = map(int, raw_input().split())
        traits.append((x, y, z, i))

    thing = list(itertools.combinations(traits, 5))

    for i in thing:
        A,B,C,D,E = i
        group = zip(A,B,C,D,E)
        group[0] = sum(group[0])/c*100
        group[1] = sum(group[1])/s*100
        group[2] = sum(group[2])/p*100
        group.pop(-1)
        check = min(group)
        if check > minimum:
            minimum = check

    if minimum >= 100:
        print 100.0
    else:
        print round(minimum, 1)

