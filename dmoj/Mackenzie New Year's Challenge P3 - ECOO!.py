n = int(raw_input())
general = []
girls = []
dict1 = {}
ans = []


for i in xrange(n):
    s, t, p = raw_input().split()
    p = int(p)
    if t == "general":
        general.append((s, p))
    else:
        general.append((s, p))
        girls.append((s , p))
        dict1[p] = s

general.sort(key = lambda x: x[1], reverse = True)
girls.sort(key = lambda x: x[1], reverse = True)

if len(general) + len(girls) == 0:
    print "No ECOO :("
else:
    if len(general) == 0:
        pass
    elif len(general) == 1:
        if general[0][1] in dict1:
            girls.remove((general[0][0], general[0][1]))
            
        ans.append(general[0][0])
        
    else:
        if general[0][1] in dict1:
            girls.remove((general[0][0], general[0][1]))

        ans.append(general[0][0])
        
        if general[1][1] in dict1:
            girls.remove((general[1][0], general[1][1]))

        ans.append(general[1][0])

    if len(girls) > 0:
        ans.append(girls[0][0])

    ans.sort()

    print "\n".join(ans)
