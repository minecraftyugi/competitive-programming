from datetime import *

x1, y1 = map(int, raw_input().split())
x2, y2 = map(int, raw_input().split())
current = raw_input()
d = datetime.strptime(current, "%Y:%m:%d:%H:%M:%S")
add = timedelta(seconds = abs(x2-x1) + abs(y2-y1))
print str(d + add).replace("-", ":").replace(" ", ":")
