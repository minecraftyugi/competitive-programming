numbers = map(int, raw_input().split())
rows = numbers[0]
columns = numbers[1]
matrix = [[1 for x in xrange(columns + 1)] for x in xrange(rows + 1)]
num = int(raw_input())
cats = []
check1 = 0
check2 = 0

for i in range(num):
    coords = map(int, raw_input().split())
    x = coords[0]
    y = coords[1]
    cats.append((x, y))

for i in cats:
    x = i[0]
    y = i[1]
    matrix[x][y] = 0

for i in xrange(1, columns + 1):
    if matrix[1][i] == 0:
        check1 = 1
    if check1 == 1:
        matrix[1][i] = 0

for i in xrange(1, rows + 1):
    if matrix[i][1] == 0:
        check2 = 1
    if check2 == 1:
        matrix[i][1] = 0

for i in xrange(2, rows + 1):
    for j in xrange(2, columns + 1):
        if matrix[i][j] == 0:
            continue
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

print matrix[rows][columns]
