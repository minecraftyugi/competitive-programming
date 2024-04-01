num = ""
numX = 0
numY = 0
bound = raw_input()
bound = bound.split(" ")
boundX = int(bound[0])
boundY = int(bound[1])

while num != "0 0":
    num = raw_input()
    if num == "0 0":
        break
    num = num.split(" ")
    numX = int(num[0]) + numX
    numY = int(num[1]) + numY
    if numX > boundX:
        numX = boundX
    if numX < 0:
        numX = 0
    if numY > boundY:
        numY = boundY
    if numY < 0:
        numY = 0
    print str(numX)+" "+str(numY)
    
