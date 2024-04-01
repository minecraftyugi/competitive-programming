tine = int(raw_input())
space = int(raw_input())
height = int(raw_input())
top = ""
x = ""

if(tine is 0 and space is 0 and height is 0):
    print "***"
else:
    for i in xrange(space):
        y = x
        x = y + " "
        
    for i in xrange(tine):
        top = "*" + x + "*" + x + "*"
        print top
        
    row = len(top)
    print "*" * row

    for i in xrange(height):
        print x + " *"
