from sys import*
from math import*
a=raw_input()
b=raw_input()
d={}
for i in b:
    try:d[i]+=1
    except:d[i]=1
for i in a:
    try:
        d[i]-=1
        if d[i]<0:print 0;exit()
    except:print 0;exit()
print factorial(len(b)-len(a)+1)/reduce(lambda x,y:x*y,[factorial(x)for x in d.values()])%int(1e9+7)
