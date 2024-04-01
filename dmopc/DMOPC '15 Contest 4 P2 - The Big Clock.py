h, m = map(int, raw_input().split())
n = input()

m += n
addHours = m / 60
m %= 60
h += addHours
h %= 24

print h, m
