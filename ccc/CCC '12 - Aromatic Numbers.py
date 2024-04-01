string = raw_input()
ans = 0
dict1 = { "I" : 1,
          "V" : 5,
          "X" : 10,
          "L" : 50,
          "C" : 100,
          "D" : 500,
          "M" : 1000
        }

previousA = 0
previousR = 2000

for i in xrange(0, len(string), 2):
    a = int(string[i])
    r = dict1[string[i + 1]]
    if r > previousR:
        ans -= 2 * previousA * previousR

    ans += a * r
    previousA = a
    previousR = r

print ans
