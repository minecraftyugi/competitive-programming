import sys
raw_input = sys.stdin.readline
n = int(raw_input())
print len(set(sys.stdin.read().strip().split("\n")))
