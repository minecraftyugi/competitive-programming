num = int(raw_input())
sandwich = raw_input()
order = [0 for i in xrange(num+1)]
lastIndex = num
startIndex = 1

for i in xrange(num - 1, -1, -1):
    pos = sandwich[i]
    if pos == "0":
        order[lastIndex] = i + 1
        lastIndex -= 1
    else:
        order[startIndex] = i + 1
        startIndex += 1

for i in xrange(1, num + 1):
    print order[i]
