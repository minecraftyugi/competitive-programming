num = int(raw_input())
numList = map(int, raw_input().split())
counts = [1]
index = 0


for i in xrange(num - 1):
    if abs(numList[i] - numList[i + 1]) <= 2:
        counts[i - i + index] += 1
    else:
        index += 1
        counts.append(1)

print max(counts)
