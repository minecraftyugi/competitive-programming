n = int(raw_input())
k = int(raw_input())
count = n

while 1:
    if n < k:
        break
    number = n / k
    count += number
    n = number + n % k

print count
