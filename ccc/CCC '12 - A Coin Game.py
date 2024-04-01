def move(list1, number, index):
    send = []
    for i in xrange(index-1,index+2):
        original = list(list1)
        if i == index or i < 0 or i > n-1:
            send += [0]
        elif len(original[i]) > 0:
            if original[i][-1] < number:
                send += [0]
            else:
                original[i] = original[i] + (number,)
                send += [tuple(original)]
        else:
            original[i] = original[i] + (number,)
            send += [tuple(original)]

    return send

def transform(starts, end, count, visited):
    new = set()
    
    if len(starts) == 0:
        return "IMPOSSIBLE"

    for start in starts:
        if start == end:
            return count

        for position in xrange(n):
            newList = list(start)
            try:
                last = newList[position][-1]
                newList[position] = newList[position][:-1]
            except IndexError:
                continue

            add = move(newList, last, position)
            for thing in add:
                if thing != 0:
                    if thing not in visited:
                        visited.add(thing)
                        new.add(thing)

    count += 1       
    return transform(new, end, count, visited)

while 1:
    n = input()
    if n == 0:
        break

    order = map(int, raw_input().split())
    order = tuple([(i,) for i in order])
    print transform([order], tuple(sorted(order)), 0, set([order]))
