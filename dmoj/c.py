import sys, collections
lists = sys.stdin.read().strip().split('\n')
lists.pop(0)
dict1 = {}

counts = collections.Counter(lists).most_common()

for i in counts:
    if i[1] in dict1:
        dict1.update({i[1] : [int(i[0])]+dict1[i[1]]})
    else:
        dict1.update({i[1] : [int(i[0])]})
    if len(dict1) > 2:
        break

if len(dict1[max(dict1)]) > 1:
    values = dict1[max(dict1)]
    print max(values) - min(values)
else:
    high = dict1[max(dict1)][0]
    del dict1[max(dict1)]
    if len(dict1[max(dict1)]) > 1:
        numList = [abs(high - max(dict1[max(dict1)])), abs(high - min(dict1[max(dict1)]))]
        print max(numList)
    else:
        print abs(high - dict1[max(dict1)][0])
        
