import string
n = int(raw_input())
numbers = []
ans = []

for i in range(n):
    numbers.append(int(raw_input()))
    
index = numbers[0]

while 1:
    letter = numbers[index]
    if letter != 0:
        letters = [0] + list(string.ascii_uppercase)
        ans.append(letters[letter])
        if numbers[index + 1] != 0:
            index += numbers[index + 1] + 1
        else:
            print "".join(ans)
            break
    else:
        print "".join(ans)
        break

"""
from sys import*
a=map(int,stdin.read().split("\n")[1:-1])
i=a[0]
b=[]
def e():print`b`[2::5];exit()
while 1:
    c=a[i]
    if c:
        b+=chr(c+64),
        d=a[i+1]
        if d:i+=d+1 
        else:e()
    else:e()    
"""
