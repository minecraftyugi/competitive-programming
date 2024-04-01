n = input()
lists = map(int, raw_input().split())
count = 0

for index, value in enumerate(lists):
    if index%2 == value%2:
        count += 1

print count
