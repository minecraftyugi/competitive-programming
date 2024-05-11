SIZE = 21
G = [[0]*SIZE for _ in range(SIZE)]
G[0][0] = 1

for i in range(SIZE):
    for j in range(SIZE):
        if i == 0 and j != 0:
            G[i][j] += G[i][j-1]
        elif j == 0 and i != 0:
            G[i][j] += G[i-1][j]
        elif i != 0 and j != 0:
            G[i][j] += G[i-1][j] + G[i][j-1]

print(G[SIZE-1][SIZE-1])
