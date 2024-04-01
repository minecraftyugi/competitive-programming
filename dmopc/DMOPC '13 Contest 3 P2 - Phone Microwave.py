from datetime import *

s = input()
current = raw_input()
d = datetime.strptime(current, "%Y/%m/%d %H:%M:%S")
subtract = timedelta(hours = s)
print str(d - subtract).replace("-", "/")
