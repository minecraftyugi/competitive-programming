import itertools
team = int(raw_input())
num = int(raw_input())
dict1 = { 1 : 0,
          2 : 0,
          3 : 0,
          4 : 0
        }
total = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
count = 0

for i in xrange(num):
    score = map(int, raw_input().split())
    if score[2] > score[3]:
        dict1[score[0]] += 3
    elif score[2] < score[3]:
        dict1[score[1]] += 3
    else:
        dict1[score[0]] += 1
        dict1[score[1]] += 1
    total.remove((score[0],score[1]))

lists = list(itertools.product([(0,3),(1,1),(3,0)], repeat = len(total)))

for i in xrange(len(lists)):
    dict2 = dict1.copy()
    for j in xrange(len(total)):
        dict2[total[j][0]] += lists[i][j][0]
        dict2[total[j][1]] += lists[i][j][1]
    if dict2[team] <= dict2[1] and team != 1:
        continue
    if dict2[team] <= dict2[2] and team != 2:
        continue
    if dict2[team] <= dict2[3] and team != 3:
        continue
    if dict2[team] <= dict2[4] and team != 4:
        continue
    count += 1

print count
