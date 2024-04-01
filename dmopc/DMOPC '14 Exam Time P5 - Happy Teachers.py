n = input()
teachers = []

for i in xrange(n):
    h, e, p = map(int, raw_input().split())
    teachers.append((h, e, p))

s = input()
duration = [0]*1001
prep = [0]*1001

for h, e, p in teachers:
    for i in xrange(s, -1, -1):
        count = 0
        happy = h
        time = p
        while i - time >= 0:
            if h - count * e <= 0:
                break

            if happy + prep[i-time] > prep[i]:
                prep[i] = happy + prep[i-time]
                duration[i] = duration[i-time] + count + 1
            elif happy + prep[i-time] == prep[i]:
                duration[i] = min(duration[i], duration[i-time] + count + 1)

            count += 1
            time += p
            happy += h - count * e

print prep[s]
print duration[s]
