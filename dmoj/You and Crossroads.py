n = input()
q1, q2, q3, q4 = 0, 0, 0, 0

for i in xrange(2*n):
    line = raw_input()
    if i < n:
        for index, char in enumerate(line):
            if index < n:
                q2 += 1 if char == "g" else 0
            else:
                q1 += 1 if char == "g" else 0
    else:
        for index, char in enumerate(line):
            if index < n:
                q3 += 1 if char == "g" else 0
            else:
                q4 += 1 if char == "g" else 0

list1 = [(q1, 1), (q2, 2), (q3, 3), (q4, 4)]
list1.sort(key = lambda x:x[1])
list1.sort(key = lambda x:x[0], reverse=True)
print list1[0][1]
