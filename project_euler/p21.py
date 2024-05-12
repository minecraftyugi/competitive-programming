MAX_N = 10000

def get_proper_divisor_sum(n):
    total = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
            
    return total

divisor_sums = [0] * (4*MAX_N+1)
for i in range(2, 4*MAX_N):
    divisor_sums[i] = get_proper_divisor_sum(i)

ans = 0
for i in range(2, MAX_N):
    if divisor_sums[divisor_sums[i]] == i and i != divisor_sums[i]:
        ans += i

print(ans)
