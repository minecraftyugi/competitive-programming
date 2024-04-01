n = input()
vets = []

for i in xrange(n):
    name, amount = raw_input().split()
    amount = int(amount)
    vets.append((name, amount))

q = input()

for i in xrange(q):
    skill, d = map(int, raw_input().split())
    best = []
    for name, value in vets:
        if 0 <= value - skill <= d:
            best.append((name, value - skill))

    best.sort(key = lambda x: x[1])

    if len(best) == 0:
        print "No suitable teacher!"
    else:
        print best[0][0]
