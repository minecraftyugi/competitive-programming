a = input()
b = input()
n = input()
word = raw_input()[:-1]
counter = [0]*8192
d = {}
for i in xrange(len(word) - a + 1):
    num = int("1" + word[i:i+a], 2)
    counter[num] += 1
    for j in xrange(i+a, min(i+b, len(word))):
        num *= 2
        num += int(word[j])
        counter[num] += 1

for i in xrange(8191, -1, -1):
    if counter[i]:
        d.setdefault(counter[i], []).append(i)
        
frequencies = sorted(d.items(), reverse=True)
def formatter(l):
    s = ""
    for i in l:
        s += bin(i)[3:] + " "

    return s

for i in xrange(min(n, len(frequencies))):
    print frequencies[i][0], formatter(frequencies[i][1])
