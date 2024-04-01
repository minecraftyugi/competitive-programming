import sys
raw_input = sys.stdin.readline
n = int(raw_input())
stations = sys.stdin.read().strip().split("\n")

try:
    a = stations.index("Leslie")
    b = stations.index("Bessarion")
    c = stations.index("Bayview")
    if b - a == 1 and c - b == 1:
        print "Y"
    elif b - a == -1 and c - b == -1:
        print "Y"
    else:
        print "N"
except ValueError:
    print "N"
