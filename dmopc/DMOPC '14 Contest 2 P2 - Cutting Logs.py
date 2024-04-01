l = int(raw_input())
log = raw_input()
lists = [x for x in xrange(l) if log[x] == "X"]
ans = [log[:lists[0]]] if len(lists) > 0 else [log]

for i in xrange(len(lists) - 1):
    ans.append(log[lists[i]+1:lists[i+1]])

ans.append(log[lists[-1]+1:]) if len(lists) > 0 else 0

for i in xrange(l+1):
    try:
        ans.remove("")
    except ValueError:
        break

print len(ans)

for i in ans:
    print i
