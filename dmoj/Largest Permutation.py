n, k = map(int, raw_input().split())
order = map(int, raw_input().split())
indexes = [0]*(n+1)
for i in xrange(n):
    indexes[order[i]] = i

index = 0
highest = n
while k and highest:
    val = order[index]
    order[index], order[indexes[highest]] = order[indexes[highest]], order[index]
    indexes[order[index]], indexes[val] =  \
    indexes[val], indexes[order[index]]
    if val == highest:
        k += 1
        
    k -= 1
    index += 1
    highest -= 1

print " ".join(map(str, order))
