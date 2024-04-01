n, t = map(int, raw_input().split())
possible = []

for i in xrange(n):
    pp, vp, pa, va, pg, vg = map(int, raw_input().split())
    group = [(pp, vp), (pa, va), (pg, vg)]
    group.sort(key = lambda x: x[1], reverse=True)
    group.sort(key = lambda x: x[0])
    possible.append(group)

count = 0
lists = [0]

for a, b, c in possible:
    new = [0]
    
    for i in xrange(1, t + 1):
        if count == 0:
            if all([a[0] > i, b[0] > i, c[0] > i]):
                lists.append(0)
            else:
                if all([a[0] <= i, b[0] <= i, c[0] <= i]):
                    lists.append(max(c[1], lists[-1]))
                elif a[0] <= i and b[0] <= i:
                    lists.append(max(b[1], lists[-1]))
                else:
                    lists.append(a[1])
        else:
            if all([a[0] > i, b[0] > i, c[0] > i]):
                new.append(lists[i])
            else:
                if all([a[0] <= i, b[0] <= i, c[0] <= i]):
                    new.append(max(c[1] + lists[i - c[0]], b[1] + lists[i - b[0]], a[1] + lists[i - a[0]], lists[i]))
                elif a[0] <= i and b[0] <= i:
                    new.append(max(b[1] + lists[i - b[0]], a[1] + lists[i - a[0]], lists[i]))
                else:
                    new.append(max(a[1] + lists[i - a[0]], lists[i]))

    if count > 0:
        lists = new[:]
        
    count += 1

print lists[-1]
