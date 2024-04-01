n = input()
t = input()
left = [0]
right = [0]
for i in xrange(n):
    pumpkin = input()
    if pumpkin < 0:
        left.append(abs(pumpkin))
    else:
        right.append(pumpkin)

left.sort()
right.sort()
ans = 10000
for i in xrange(min(t, len(right) - 1), 0, -1):
    if t - i == len(left):
        break

    if i == t:
        ans = min(ans, right[i])
    else:
        ans = min(ans, 2 * right[i] + left[t-i])

for i in xrange(min(t, len(left) - 1), 0, -1):
    if t - i == len(right):
        break

    if i == t:
        ans = min(ans, left[i])
    else:
        ans = min(ans, 2 * left[i] + right[t-i])

print ans
