n = input()
lists = []
dp = [[0 for i in xrange(n)]for i in xrange(n)]

for i in xrange(n):
    time, weight = map(int, raw_input().split())
    lists.append((time, weight))

for i in xrange(n):
    for j in xrange(n):
        if i + j > n:
            break
        
        possible = []
        for k in xrange(j, i+j+1):
            if k == j:
                if k == i+j:
                    time, weight = lists[k]
                    possible.append(time * weight)
                else:
                    
            
