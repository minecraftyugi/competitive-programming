BOUND = 28123

def get_proper_divisor_sum(n):
    total = 1
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            total += i
            total += n // i
            if i == n // i:
                total -= i

    return total

divisor_sums = [0] * (BOUND+1)
for i in range(2, BOUND+1):
    divisor_sums[i] = get_proper_divisor_sum(i)

abundant_numbers = []
for i in range(2, BOUND+1):
    if divisor_sums[i] > i:
        abundant_numbers.append(i)

valid = [0] * (BOUND+1)
for i in range(len(abundant_numbers)):
    x = abundant_numbers[i]
    for j in range(i, len(abundant_numbers)):
        y = abundant_numbers[j]
        if x + y > BOUND:
            break
        valid[x+y] = 1

ans = 0
for i in range(BOUND+1):
    if valid[i] != 1:
        ans += i

print(ans)
