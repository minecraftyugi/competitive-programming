line = map(int, raw_input().split())
num = line[0]
leaders = line[1]
position = line[2]
ranks = map(int, raw_input().split())
ranks.sort(reverse=True)
maximum = 0

for i in range(position - 1, num, leaders):
    maximum += ranks[i]

print maximum
