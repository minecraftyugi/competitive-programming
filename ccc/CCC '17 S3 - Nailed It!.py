n = input()
lengths = map(int, raw_input().split())
boards = [0]*2001
heights = [0]*4001

for i in lengths:
    boards[i] += 1

for i in xrange(2001):
    for j in xrange(i, 2001):
        if i == j:
            heights[i+j] += boards[i] / 2
        else:
            heights[i+j] += min(boards[i], boards[j])

max_height = 0
num_ways = 0
for height in heights:
    if height > max_height:
        max_height = height
        num_ways = 1
    elif height == max_height:
        num_ways += 1

print max_height, num_ways
