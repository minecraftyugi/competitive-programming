n = input()
while n:
    rows = [set()for i in xrange(n)]
    columns = [set()for i in xrange(n)]
    check = True
    for i in xrange(n):
        line = map(int, raw_input().split())
        for j in xrange(n):
            num = line[j]
            if num < 1 or num > n:
                check = False
                
            columns[j].add(num)
            rows[i].add(num)

    for i in xrange(n):
        if len(rows[i]) != n or len(columns[i]) != n:
            check = False

    print ["no", "yes"][check]
    n = input()
