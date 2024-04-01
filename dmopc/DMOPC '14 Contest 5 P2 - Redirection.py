n = input()
lists = []

for i in xrange(n):
    lists.append(raw_input())

m = input()
times = [0] * m

for word in lists:
    minimum = min(times)

    if minimum != 0:
        times = map(lambda x: x - minimum, times)

    index = times.index(0)
    times[index] += len(word)
    print index + 1
