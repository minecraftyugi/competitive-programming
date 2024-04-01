import math
number = int(raw_input())
num = list(str(math.floor(math.sqrt(number))))
num.pop(len(num) - 1) and num.pop(len(num) - 1)
num = "".join(num)
print "The largest square has side length "+str(num)+"."
