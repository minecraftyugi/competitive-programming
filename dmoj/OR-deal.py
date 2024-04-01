n = input()
start = 2

while start <= n:
    start *= 2

print str(bin(start - 1))[2:]
