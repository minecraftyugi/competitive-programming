import sys
raw_input = sys.stdin.readline

n = int(raw_input())
take = 0
serve = 0

while 1:
    word = raw_input().strip()
    if word == "EOF":
        break
    elif word == "TAKE":
        take += 1
        n += 1
        n %= 999
    elif word == "SERVE":
        serve += 1
    else:
        print take, take - serve, n
        serve = 0
        take = 0
