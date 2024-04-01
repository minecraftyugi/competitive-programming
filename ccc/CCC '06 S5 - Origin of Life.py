m, n, a, b, c = map(int, raw_input().split())
original_gen = ""
for i in range(m):
    line = raw_input().replace(".", "0").replace("*", "1")
    original_gen += line

original_gen = int(original_gen, 2)

def next_gen(config):
    new_config = 0
    for i in range(m):
        for j in range(n):
            live = 0
            for k in range(max(0, i-1), min(m, i+2)):
                for l in range(max(0, j-1), min(n, j+2)):
                    if not (i == k and j == l):
                        if config & (1 << ((m-1 - k) * n + n-1 - l)):
                            live += 1

            if config & (1 << ((m-1 - i) * n + n-1 - j)):
                if live >= a and live <= b:
                    new_config |= 1 << ((m-1 - i) * n + n-1 - j)
            else:
                if live > c:
                    new_config |= 1 << ((m-1 - i) * n + n-1 - j)

    return new_config
                    
G = [[] for i in range(2**(m*n))]
eden = [1]*2**(m*n)
for i in range(2**(m*n)):
    next_generation = next_gen(i)
    G[next_generation].append(i)
    eden[next_generation] = 0

def traverse():  
    start = original_gen
    if eden[start]:
        return 0
    
    q = [start]
    visited = [0]*2**(m*n)
    visited[start] = 1
    count = 1
    while q:
        new_q = []
        while q:
            gen = q.pop()
            print gen, G[gen]
            for pre_gen in G[gen]:
                if not visited[pre_gen]:
                    visited[pre_gen] = 1
                    new_q.append(pre_gen)

                if eden[pre_gen]:
                    return count

        q = new_q[:]
        count += 1

    return -1

print traverse()
