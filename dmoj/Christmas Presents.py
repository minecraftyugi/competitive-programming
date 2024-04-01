p = input()
t = input()
dict1 = {}
dict2 = {}
teachers = []

for i in xrange(p):
    name = raw_input()
    price = float(raw_input())
    dict1[price] = name

presents = dict1.items()
presents.sort(key = lambda x: x[0])

for i in xrange(t):
    name = raw_input()
    rating = int(raw_input())
    teachers.append((rating, name))

teachers.sort(key = lambda x: x[0])

for i in xrange(t):
    print teachers[i][1], "will get a", presents[i][1]
