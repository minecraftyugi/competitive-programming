num = int(raw_input())
lists = []
mins = 0

for i in range(num):
    lists.append(int(raw_input()))

lists.sort(reverse=True)
mins += (lists[0] + lists[1]) * 2

for i in xrange(2, num):
    mins += lists[i]
    
print mins + 10

