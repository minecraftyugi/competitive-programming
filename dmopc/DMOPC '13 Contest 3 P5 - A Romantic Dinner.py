#m = time, u = amount
m, u, r = map(int, raw_input().split())
options = []
dict1 = {}

for i in xrange(r):
    v, t, f = map(int, raw_input().split())
    options.append((v, t, f))

count = 0
dict1[0] = [[0 for i in xrange(u+1)], [0]]

for value, time, amount in options:
    dict1[1] = [[0 for i in xrange(u+1)], [0]]

    for i in xrange(1, m + 1):
        for j in xrange(1, u + 1):
            if count == 0:
                if i - time < 0 or j - amount < 0:
                    dict1[0][-1].append(0)
                else:
                    dict1[0][-1].append(value)
            else:
                if i - time < 0 or j - amount < 0:
                    dict1[1][-1].append(dict1[0][i][j])
                else:
                    best = max(value + dict1[0][i - time][j - amount], dict1[0][i][j])
                    dict1[1][-1].append(best)

        if count == 0:
            dict1[0].append([0])
        else:
            dict1[1].append([0])

    if count != 0:
        dict1[0] = dict1[1]
        
    count += 1

print dict1[1][-2][-1] if count != 1 else dict1[0][-2][-1]
