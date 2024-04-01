import math
start = int(raw_input())
stop = int(raw_input())
count = 0
start = int(math.ceil(math.sqrt(start)))
stop = int(math.floor(math.sqrt(stop)))

for i in xrange(start, stop + 1):
    square = i**2
    cubic = square**(1/3.0)
    #print "SQUARE :"+str(square)+" CUBIC :"+str(cubic)
    cubeList = str(cubic)
    if cubeList[len(cubeList) - 1] == "0" and cubeList[len(cubeList) - 2] == ".":
        count += 1
    else:
        continue

print count
