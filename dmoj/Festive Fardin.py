import sys
shirt = raw_input().split()
pants = raw_input().split()
count = 0

if "red" in shirt or "green" in shirt or "white" in shirt:
    count += 1
if "red" in pants or "green" in pants or "white" in pants:
    count += 1

print "Jingle Bells" if count == 2 else "Boring..."
