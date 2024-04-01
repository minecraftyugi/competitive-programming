MIN = 0
MAX = 1
dp_max = [[[[-1]*31 for _ in range(31)] for _ in range(31)] for _ in range(31)]
dp_min = [[[[-1]*31 for _ in range(31)] for _ in range(31)] for _ in range(31)]

def minimax(player, state):
    w, x, y, z = state
    moves = next_states(state)
    if player == MAX:
        if end(moves):
            ans = 0
        else:
            ans = 0
            for move in moves:
                a, b, c, d = move
                if dp_min[a][b][c][d] == -1:
                    dp_min[a][b][c][d] = minimax(MIN, move)
                    
                ans = max(ans, dp_min[a][b][c][d])
    else:
        if end(moves):
            ans = 1
        else:
            ans = 1
            for move in moves:
                a, b, c, d = move
                if dp_max[a][b][c][d] == -1:
                    dp_max[a][b][c][d] = minimax(MAX, move)
                    
                ans = min(ans, dp_max[a][b][c][d])

    if player == MAX:
        dp_max[w][x][y][z] = ans
    else:
        dp_min[w][x][y][z] = ans
        
    return ans

def next_states(state):
    possible = []
    copy = state[:]
    if state[0] >= 2 and state[1] >= 1 and state[3] >= 2:
        copy[0] -= 2
        copy[1] -= 1
        copy[3] -= 2
        possible.append(copy)

    copy = state[:]
    if state[0] >= 1 and state[1] >= 1 and state[2] >= 1 and state[3] >= 1:
        copy[0] -= 1
        copy[1] -= 1
        copy[2] -= 1
        copy[3] -= 1
        possible.append(copy)

    copy = state[:]
    if state[2] >= 2 and state[3] >= 1:
        copy[2] -= 2
        copy[3] -= 1
        possible.append(copy)

    copy = state[:]
    if state[1] >= 3:
        copy[1] -= 3
        possible.append(copy)

    copy = state[:]
    if state[0] >= 1 and state[3] >= 1:
        copy[0] -= 1
        copy[3] -= 1
        possible.append(copy)

    return possible

def end(moves):
    return len(moves) == 0

n = input()
for i in range(n):
    state = map(int, raw_input().split())
    if minimax(MAX, state):
        print "Patrick"
    else:
        print "Roland"
