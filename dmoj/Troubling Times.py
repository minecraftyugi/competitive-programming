n, d = map(int, raw_input().split())
intervals = map(int, raw_input().split())
intervals.sort(reverse=True)
found = False

for interval in intervals:
    if d % interval == 0:
        print abs(d / interval)
        found = True
        break
    
if not found:
    print "This is not the best time for a trip."
