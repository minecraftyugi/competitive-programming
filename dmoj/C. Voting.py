import collections

n = input()
order = raw_input()
indexes = range(n)
d = []
r = []
for i in range(n):
    if order[i] == "D":
        d.append(i)
    else:
        r.append(i)

while len(d) != 0 and len(r) != 0:
    new_indexes = []
    new_d = collections.deque()
    new_r = collections.deque()
    d.reverse()
    r.reverse()
    for index in indexes:
        if len(d) > 0 and d[-1] == index:
            if len(r) != 0:
                r.pop()
            elif len(new_r) != 0:
                new_r.popleft()
                
            new_d.append(d.pop())
            new_indexes.append(index)
        elif len(r) > 0 and r[-1] == index:
            if len(d) != 0:
                d.pop()
            elif len(new_d) != 0:
                new_d.popleft()

            new_r.append(r.pop())
            new_indexes.append(index)

    indexes = new_indexes[:]
    d = list(new_d)
    r = list(new_r)

if len(d) == 0:
    print "R"
else:
    print "D"
