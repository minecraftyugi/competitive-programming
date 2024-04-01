c, f, s = map(int, raw_input().split())
n = input()

for i in xrange(n):
    line = raw_input().split()
    x = int(line[0])
    c1 = float(line[1])
    f1 = float(line[2])
    s1 = float(line[3])
    name = line[4:]
    if all([c1/x <= c, f1/x <= f, s1/x <= s]):
        print" ".join(name)
