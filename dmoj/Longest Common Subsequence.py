x, y = map(int, raw_input().split())
list1 = [0] + map(int, raw_input().split())
list2 = [0] + map(int, raw_input().split())
ans1 = [0 for i in xrange(y+1)]
ans2 = [0]

for i in xrange(1, x+1):
    for j in xrange(1, y+1):
        if list1[i] == list2[j]:
            ans2 += ans1[j-1] + 1,
        else:
            ans2 += max(ans1[j], ans2[-1]),

    ans1 = ans2[:]
    ans2 = [0]

print ans1[-1]
