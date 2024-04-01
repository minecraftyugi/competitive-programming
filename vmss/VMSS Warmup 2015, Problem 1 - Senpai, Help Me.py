import math

num = int(raw_input())

sqrt = int(math.ceil(math.sqrt(num)))

for i in range(sqrt, 0, -1):
    if num % i == 0:
        print (i * 2) + (2 * num / i)
        break
