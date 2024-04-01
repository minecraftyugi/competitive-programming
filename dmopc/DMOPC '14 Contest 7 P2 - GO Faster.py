import sys
raw_input = sys.stdin.readline
num = int(raw_input())
minimum, maximum = map(int, raw_input().split())
maximum += minimum
a, b = map(int, raw_input().split())
maximum -= b
minimum -= b
passengers = maximum + a

for i in xrange(num - 3):
    line = map(int, raw_input().split())
    on = line[0]
    off = line[1]
    passengers -= off
    minimum -= off
    if passengers < 0:
        maximum += passengers
    passengers += on

print minimum if minimum > 0 else 0
print maximum if maximum > 0 else 0
