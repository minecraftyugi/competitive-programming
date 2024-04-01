num = int(raw_input())
numbers = [False, False] + [i for i in xrange(2, 3164)]
primes = []

for i in xrange(2, 3164):
    if numbers[i] is not False:
        primes.append(numbers[i])
        for j in xrange(i*2, 3164, i):
            numbers[j] = False

index = 0
ans = []
while 1:
    if num % primes[index] == 0:
        ans.append(str(primes[index]))
        num /= primes[index]
    elif index == 446:
        break
    else:
        index += 1

if ans == []:
    print ""
elif num != 1:
    ans.append(str(num))
    print "\n".join(ans)
else:
    print "\n".join(ans)
