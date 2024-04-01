t = input()
good = set([(1,0), (2,0), (3,0), (2,1)])
maybe = set([(1,1), (3,1), (2,2)])
def solve(level, x, y):
    if level == 1:
        if (x, y) in good:
            return "crystal"
        else:
            return "empty"
    else:
        m = 5**(level-1)
        newx, newy = x/m, y/m
        if (newx, newy) in good:
            return "crystal"
        elif (newx, newy) in maybe:
            return solve(level-1, x%m, y%m)
        else:
            return "empty"

for i in xrange(t):
    m, x, y = map(int, raw_input().split())
    print solve(m, x, y)
