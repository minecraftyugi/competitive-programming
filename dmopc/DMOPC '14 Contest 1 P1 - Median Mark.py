n = input()
lists = []

for i in xrange(n):
    num = input()
    lists.append(num)

lists.sort()

if n % 2:
    print lists[n/2]
elif n == 1:
    print lists[0]
else:
    print sum(lists[n/2-1:n/2+1])/2+1 if sum(lists[n/2-1:n/2+1])%2 else sum(lists[n/2-1:n/2+1])/2
