num = int(raw_input())
a = 100
d = 100

for i in xrange(num):
    line = raw_input()
    line = line.split()
    if int(line[0]) > int(line[1]):
        d -= int(line[0])
    elif int(line[0]) < int(line[1]):
        a -= int(line[1])
    else:
        continue

print a
print d
