import bisect, collections

minimum = int(raw_input())
maximum = int(raw_input())
num = int(raw_input())
order = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
dict1 = collections.defaultdict(list)

for i in xrange(num):
    number = int(raw_input())
    bisect.insort(order, number)

numList = [0] * len(order)
numList[0] = 1

for i in xrange(len(order)):
    index = 1
    number = order[i]
    while 1:
        try:
            if order[i + index] - number < minimum:
                index += 1
                continue
            if order[i + index] - number > maximum:
                break
            dict1[i].append(i + index)
            index += 1
        except IndexError:
            break

for i in dict1.keys():
    for j in dict1[i]:
        numList[j] += numList[i]

print numList[-1]
