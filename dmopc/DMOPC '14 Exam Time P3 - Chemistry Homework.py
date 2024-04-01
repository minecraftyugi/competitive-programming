import sys

raw_input = sys.stdin.readline
n = input()
m = input()
g = [[]for i in xrange(n+1)]
for i in xrange(m):
    a, b = map(int, raw_input().split())
    if a != b:
        g[a].append(b)
        g[b].append(a)

valid = True
c, h = 0, 0
for i in xrange(1, n+1):
    if g[i]:
        g[i].sort()
        length = len(g[i])
        if 2 <= length <= 3 or length > 4:
            valid = False
        elif length == 4:
            if len(set(g[i][:3])) == 1 or len(set(g[i][1:])) == 1:
                valid = False
            elif len(set(g[i])) == 1:
                valid = False
            else:
                c += 1
        elif length == 1:
            if len(g[g[i][0]]) != 4:
                valid = False
            else:
                h += 1
    else:
        valid = False

if valid:
    ans = 0
    visited = [[]for i in xrange(n+1)]
    for i in xrange(n+1):
        length = len(g[i])
        if length == 1 and g[i][0] not in visited[i]:
            ans += 413
            visited[i].append(g[i][0])
            visited[g[i][0]].append(i)
        elif length == 4:
            single = 0
            double = 0
            past = []
            for j in xrange(4):
                num = g[i][j]
                if len(g[num]) == 1 and num not in visited[i]:
                    ans += 413
                    visited[i].append(num)
                    visited[num].append(i)
                elif len(g[num]) == 4 and num not in visited[i]:
                    if num in past:
                        single -= 1
                        double += 1
                    else:
                        single += 1
                        past.append(num)

            ans += single * 346
            ans += double * 615
            for node in past:
                visited[i].append(node)
                visited[node].append(i)

    print ans
    print "C{}H{}".format(["", c][c > 1], ["", h][h > 1])
else:
    print "Impossible"
