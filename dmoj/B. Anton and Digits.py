k2, k3, k5, k6 = map(int, raw_input().split())
ans = 0
total = min(k2, k5, k6)
ans += total * 256
k2 -= total
k5 -= total
k6 -= total
total = min(k2, k3)
ans += total * 32
print ans
