import collections
num = int(raw_input())
time = 0
dict1 = collections.defaultdict(int)
dict2 = collections.defaultdict(int)
dict3 = {}
lists = []

for i in xrange(num):
    thing = raw_input().split()
    letter = thing[0]
    x = int(thing[1])
    lists.append((letter, x))

for i in xrange(num):
    letter = lists[i][0]
    x = lists[i][1]
    if letter == "R":
        dict1[x] += time
        if x not in dict3:
            dict3[x] = [0,0]
        dict3[x][0] += 1
    elif letter == "W":
        time += x - 2
    else:
        dict2[x] += time - dict1[x]
        dict1[x] = 0
        dict3[x][1] += 1

    time += 1

for i in dict3.keys():
    if dict3[i][0] != dict3[i][1]:
        dict2[i] = -1

numbers = dict2.items()
numbers.sort()

for i in numbers:
    print i[0], i[1]
    
