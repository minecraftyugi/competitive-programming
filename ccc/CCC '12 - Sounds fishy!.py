lists = []
for i in range(4):
    num = int(raw_input())
    lists.append(num)

if lists[0] < lists[1] < lists[2] < lists[3]:
    print "Fish Rising"
elif lists[0] > lists[1] > lists[2] > lists[3]:
    print "Fish Diving"
elif lists[0] == lists[1] == lists[2] == lists[3]:
    print "Fish At Constant Depth"
else:
    print "No Fish"
