import sys
lists = sys.stdin.read().strip().split('\n')
#lists = ["10 3", "5 6 7 8 3 4 5 6 1 2", "1 3", "2 4", "1 10"]

shows = map(int, lists[1].split())
first = map(int, lists[0].split())
listLen = first[0]
times = first[1]
sumList = [shows[0]]

for i in range(1, listLen):
    sumList.append(shows[i] + sumList[i-1])

sumList = [0] + sumList
maximum = sumList[-1]

for i in range(2, times+2):
    tup = map(int, lists[i].split())
    print maximum - sumList[tup[1]] + sumList[tup[0]-1]
