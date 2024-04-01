num = int(raw_input())

for i in xrange(num):
    line = raw_input().split()
    count = 0
    for word in line:
        if word[0].isupper():
            count += 1
    print count
