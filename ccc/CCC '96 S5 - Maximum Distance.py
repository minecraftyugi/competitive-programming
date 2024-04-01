n = input()
def find(n, l):
    upper = len(l)
    lower = 0
    while lower < upper:
        mid = (lower + upper) / 2
        if l[mid] <= n:
            upper = mid
        else:
            lower = mid + 1

    if lower == len(l):
        return -1
    
    return l[lower]

def distance(l1, l2, length):
    d1, d2 = {}, {}
    s1, s2 = [], []
    prev = 100001
    for i in xrange(length):
        if l1[i] != prev:
            prev = l1[i]
            s1.append(prev)
            d1[prev] = i

    prev = -1
    for i in xrange(length-1, -1, -1):
        if l2[i] != prev:
            prev = l2[i]
            s2.append(prev)
            d2[prev] = i

    s2.reverse()
    maximum = 0
    for i in xrange(len(s2)-1, -1, -1):
        num = s2[i]
        num2 = find(num, s1)
        if num2 == -1:
            continue
        elif d2[num] >= d1[num2]:
            maximum = max(maximum, d2[num] - d1[num2])
        
    return "The maximum distance is {}".format(maximum)

for i in xrange(n):
    m = input()
    l1 = map(int, raw_input().split())
    l2 = map(int, raw_input().split())
    print distance(l1, l2, m)
