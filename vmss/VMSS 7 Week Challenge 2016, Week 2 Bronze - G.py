n = input()

r1 = list("GGGGG")
r2 = list("G....")
r3 = list("G..GG")
r4 = list("G...G")
r5 = list("GGGGG")
ans = []
thing = "".join([i*n for i in r1])
ans += [thing]*n
thing = "".join([i*n for i in r2])
ans += [thing]*n
thing = "".join([i*n for i in r3])
ans += [thing]*n
thing = "".join([i*n for i in r4])
ans += [thing]*n
thing = "".join([i*n for i in r5])
ans += [thing]*n

for i in ans:
    print i
