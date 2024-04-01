n, r, m = map(int, raw_input().split())
rocket = map(int, raw_input().split())
people = map(int, raw_input().split())
stops = [0]*(n+1)
rocket_count = 0
regular_count = m
for stop in rocket:
    stops[stop] = 1

index = 0
while rocket_count < m / 2 and index < m:
    if stops[people[index]]:
        rocket_count += 1
        regular_count -= 1

    index += 1

def running_sum(n):
    return n * (n+1) / 2

print running_sum(rocket_count) + running_sum(regular_count)
