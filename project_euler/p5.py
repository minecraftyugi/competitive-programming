import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

ans = 1
i = 1
while i <= 20:
    ans = lcm(ans, i)
    i += 1

print(ans)
    
        
