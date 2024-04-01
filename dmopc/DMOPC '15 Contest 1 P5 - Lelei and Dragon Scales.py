w, h, n = map(int, raw_input().split())
grid1 = [[0 for i in xrange(w+1)]for j in xrange(h+1)]
grid2 = [[0 for i in xrange(w+1)]for j in xrange(h+1)]
dict1 = {}
maximum = 0

for i in xrange(1, h+1):
    line = map(int, raw_input().split())

    for j in xrange(1, w+1):
        grid1[i][j] = grid1[i][j-1] + line[j-1]
        grid2[i][j] = grid1[i][j] + grid2[i-1][j]

for i in xrange(1, max(w,h)+1):
    num = n / i
    if num > w and num > h or num == 0:
        pass
    else:
        if num not in dict1:
            dict1[i] = num
            dict1[num] = i

for i in xrange(h, 0, -1):
    for j in xrange(w, 0, -1):
        for x, y in dict1.items():
            br = grid2[i][j]
            if i-x >= 0 and j-y >= 0:
                bl = grid2[i-x][j]
                tl = grid2[i-x][j-y]
                tr = grid2[i][j-y]
                area = br + tl - bl - tr
                maximum = area if maximum < area else maximum

print maximum
