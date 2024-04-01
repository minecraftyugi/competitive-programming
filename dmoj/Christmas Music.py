import sys
n = int(raw_input())
keys = ["","C","D","E","F","G","A","B"]
values = []
leap = 0
position = ""

for i in xrange(n):
    key = raw_input()
    note = keys.index(key[0])
    octave = int(key[1])
    actual = note + 7*(octave - 1)
    values.append(actual)

if values[0]> values[1]:
    position = "down"
else:
    position = "up"
    
if abs(values[0]-values[1])>=7:
    print "Salieri's music"
    sys.exit()
    
for i in xrange(1,n-1):
    a = values[i]
    b = values[i+1]
    if abs(b-a)>=7:
        print "Salieri's music"
        sys.exit()
    if abs(b-a)>=5 and leap == 1:
        print "Salieri's music"
        sys.exit()
    elif b-a>=5 and position == "up":
        print "Salieri's music"
        sys.exit()
    elif a-b>=5 and position == "down":
        print "Salieri's music"
        sys.exit()
    else:
        if abs(a-b)>=5:
            leap = 1
            position = "up" if b > a else "down"
        else:
            leap = 0
            position = ["down","none","up"][cmp(a,b)]
    
print "Melodious!"
