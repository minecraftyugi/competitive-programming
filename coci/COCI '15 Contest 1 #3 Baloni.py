n = input()
balloons = map(int, raw_input().split())
heights = [0]*1000002
ans = n
for balloon in balloons:
    heights[balloon] += 1
    if heights[balloon+1]:
        ans -= 1
        heights[balloon+1] -= 1

print ans
