import collections, sys
a = input()
b = input()
x = input()
primes = [0,0]+[1 for i in xrange(2, 31624)]
numbers = [2]
set1 = collections.defaultdict(int)
set2 = collections.defaultdict(int)
ans = 1

if (a == 1 and b == 1) or x == 1:
    print x
    sys.exit()
    
for i in xrange(3, 31624, 2):
    if primes[i]:
        numbers += [i]
        for j in xrange(i*i, 31624, 2*i):
            primes[j] = 0

index = 0
while 1:
    if index == 3401:
        set1[a] = 1
        break
    num = numbers[index]
    if num > a:
        set1[a] = 1
        break
    else:
        if a % num == 0:
            set1[num] += 1
            a /= num
        else:
            index += 1

index = 0
while 1:
    if index == 3401:
        set2[b] = 1
        break
    num = numbers[index]
    if num > b:
        set2[b] = 1
        break
    else:
        if b % num == 0:
            set2[num] += 1
            b /= num
        else:
            index += 1

for number in set1:
    if number not in set2:
        ans *= number * set1[number]

for number in set2:
    if number not in set1:
        ans *= number * set2[number]
    else:
        ans *= number * max(set1[number], set2[number])

if x % ans == 0:
    print x / ans
else:
    print x / ans + 1
