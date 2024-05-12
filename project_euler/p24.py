import math

N = 999_999
digits = [i for i in range(10)]
ans = 0
n = N
while n > 0:
    i = 0
    permutations = math.factorial(len(digits)-1)
    while n - permutations >= 0:
        i += 1
        n -= permutations

    ans *= 10
    ans += digits[i]
    digits.remove(digits[i])

for digit in digits:
    ans *= 10
    ans += digit
    
print(ans)
