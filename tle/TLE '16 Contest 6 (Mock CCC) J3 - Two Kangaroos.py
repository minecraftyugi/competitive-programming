x1, y1, k = map(int, raw_input().split())
x2, y2, l = map(int, raw_input().split())

steps = 0
x_diff = abs(x1 - x2)
y_diff = abs(y1 - y2)
hop_d = max(k - l, l - 1)
steps += x_diff / hop_d
steps += y_diff / hop_d
if x_diff % hop_d != 0:
    steps += 1

if y_diff % hop_d != 0:
    steps += 1

print steps
