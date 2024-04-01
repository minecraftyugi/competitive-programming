n = input()
flows = []

for i in xrange(n):
    flows.append(input())

while 1:
    num = input()

    if num == 99:
        river = input()
        lflow = input() * 0.01
        rflow = 1 - lflow
        flows.insert(river, 0)
        currentFlow = flows[river - 1]
        flows[river-1] *= lflow
        flows[river] = currentFlow * rflow
    elif num == 88:
        river = input()
        flows[river-1] += flows[river]
        flows.pop(river)
    else:
        break

print " ".join(map(str, map(int, map(round, flows))))
