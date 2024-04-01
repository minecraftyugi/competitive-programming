number = int(raw_input())

def maze(start, end, graph, count):
    new = []
    if end in start:
        return count
    if list(start) == []:
        return -1
    for place in start:
        try:
            lists = graph[place]
            for i in lists:
                new.append(i)
            del graph[place]
        except KeyError:
            pass
    new = set(new)
    return maze(new, end, graph, count + 1)
    
for i in xrange(number):
    rows = int(raw_input())
    columns = int(raw_input())
    dict1 = {(r , c) : [] for r in xrange(1, rows + 1) for c in xrange(1, columns + 1)}
    for j in xrange(1, rows + 1):
        pass
    for j in xrange(1, rows + 1):
        lines = raw_input()
        for k in xrange(1, columns + 1):
            if lines[k - 1] == "+":
                if k < columns:
                    dict1[(j, k)].append((j, k + 1))
                if k > 1:
                    dict1[(j, k)].append((j, k - 1))
                if j < rows:
                    dict1[(j, k)].append((j + 1, k))
                if j > 1:
                    dict1[(j, k)].append((j - 1, k))
            elif lines[k - 1] == "-":
                if k < columns:
                    dict1[(j, k)].append((j, k + 1))
                if k > 1:
                    dict1[(j, k)].append((j, k - 1))
            elif lines[k - 1] == "|":
                if j < rows:
                    dict1[(j, k)].append((j + 1, k))
                if j > 1:
                    dict1[(j, k)].append((j - 1, k))
            else:
                for thing in dict1.keys():
                    if (j, k) in dict1[thing]:
                        dict1[thing].remove((j, k))

    print maze([(1, 1)], (rows, columns), dict1, 1)
