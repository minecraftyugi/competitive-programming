n = input()
lists = []
waCount = 0
waCount2 = 0.0
irCount = 0

for i in xrange(n):
    code = raw_input()
    if code == "WA":
        waCount += 1
        
    lists.append(code)

for index, value in enumerate(lists):
    if value == "WA":
        waCount2 += 1
        if waCount2 / waCount <= 0.3:
            lists[index] = "AC"
    elif value == "TLE":
        lists[index] = "WA"
    elif value == "IR":
        irCount += 1
        if irCount <= 10:
            lists[index] = "AC"
        elif irCount <= 20:
            lists[index] = "WA"
        else:
            pass
    else:
        pass

print "\n".join(lists)
