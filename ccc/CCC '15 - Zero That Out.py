import sys
raw_input = sys.stdin.reaadline
num = int(raw_input())
lists = []

for i in xrange(num):
    number = int(raw_input())
    try:
        if number == 0:
            lists.pop(-1)
        else:
            lists.append(number)
    except IndexError:
        pass

print sum(lists)
