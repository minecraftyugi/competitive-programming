import sys

low = 1
high = 2 * 10 ** 9
while 1:
    print (low + high) / 2
    sys.stdout.flush()
    n = raw_input()
    
    if n == "SINKS":
        low = (low + high) / 2 + 1
    elif n == "FLOATS":
        high = (low + high) / 2 - 1
    else:
        break
