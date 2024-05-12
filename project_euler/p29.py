MAX_A = 100
MAX_B = 100

distinct = set()
for a in range(2, MAX_A + 1):
    for b in range(2, MAX_B + 1):
        distinct.add(a ** b)

print(len(distinct))
