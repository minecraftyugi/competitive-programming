num = int(raw_input())
dict1 = {}

for i in range(num):
    thing = raw_input().split()
    manga = thing[0]
    number = float(thing[1])
    dict1[number] = manga

best = max(dict1)
print dict1[best]
