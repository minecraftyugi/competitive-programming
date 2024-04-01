k, d = map(int, raw_input().split())
d1, d2 = map(int, raw_input().split())
p1, p2 = map(int, raw_input().split())
visited = [[0]*k for i in xrange(k)]
primes = [1]*1001
primes[0] = 0
primes[1] = 0
for i in xrange(2, 33):
    if primes[i]:
        for j in xrange(i*i, 1001, i):
            primes[j] = 0

def adjust(dist1, dist2):
    if dist1 < dist2:
        if dist2 - dist1 < d:
            return dist1, (dist1 + d) % k
        elif dist2 > k / 2 and (k - dist2) + dist1 < d:
            return dist1, (dist1 - d) % k
    else:
        if dist1 - dist2 < d:
            return dist1, (dist1 - d) % k
        elif dist1 > k / 2 and (k - dist1) + dist2 < d:
            return dist1, (dist1 + d) % k

    return dist1, dist2

def dist(point):
    if point <= k / 2:
        return point
    else:
        return k - point

p1, p2 = adjust(p1, p2)
visited[p1][p2] = 1
p1, p2 = adjust((p1 + d1) % k, (p2 + d2) % k)
prime_d = False
while not visited[p1][p2] and not prime_d:
    if primes[dist(p1) + dist(p2)]:
        prime_d = True
        
    visited[p1][p2] = 1
    p1, p2 = adjust((p1 + d1) % k, (p2 + d2) % k)
    
if prime_d:
    print "Alice"
else:
    print "Bob"
