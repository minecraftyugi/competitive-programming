#get rid of sys in case of error reading input
#time complexity O(n)
#runs faster in pypy2, code compiles in python 2.7.8

import bisect, sys
raw_input = sys.stdin.readline

start = int(raw_input())
end = int(raw_input())
n = int(raw_input())
stops = []

for i in xrange(n):
    stop = int(raw_input())
    if stop > end:
        break
    else:
        stops.append(stop)

stops.append(end)
index = bisect.bisect(stops, start)
total = [0]*(end+1)
total[start] = [0, 5]

for i in xrange(start+1, end+1):
    if i < start + 5:
        if i == stops[index]:
            thing = [total[start][0], total[start][1] - i]
            if thing[1] + stops[index] >= stops[index+1]:
                total[i] = thing
            else:
                total[i] = [1,5]

            index += 1
        else:
            total[i] = [total[start][0], total[start][1] - i]
    else:
        if i == stops[index]:
            thing = [total[i-1][0], total[i-1][1] - 1]
            if stops[index] == end:
                total[i] = thing
            elif thing[1] + stops[index] >= stops[index+1]:
                total[i] = thing
            else:
                total[i] = [total[i-1][0] + 1, 5]

            index += 1
        else:
            total[i] = [total[i-1][0], total[i-1][1] - 1]

print total[-1][0]
