import sys, collections, bisect

raw_input = sys.stdin.readline
n = input()
bids = collections.defaultdict(list)
max_bids = []

def parent(start, visited):
    if start not in max_d or max_d[start] == start:
        for node in visited:
            if node in max_d:
                max_d[node] = start
        return start

    visited.add(max_d[start])
    return parent(max_d[start], visited)

for i in xrange(n):
    person, bid = map(int, raw_input().split())
    bids[person].append(bid)

for person in bids:
    max_bids.append((person, bids[person][-1], bids[person]))

num_bidders = len(bids)
max_d = {i:i for i in xrange(num_bidders)}
max_bids.sort(key = lambda x: x[1], reverse = True)
people = {max_bids[i][0]:i for i in xrange(num_bidders)}
q = input()
for i in xrange(q):
    remove = map(int, raw_input().split())[1:]
    for person in remove:
        if person in bids:
            parent1 = parent(people[person]+1, set([people[person]+1]))
            parent2 = parent(people[person], set([people[person]]))
            max_d[parent2] = parent1

    parent(0, set([0]))
    if max_d[0] == num_bidders:
        print 0, 0
    elif n == 1:
        print max_bids[0][0], max_bids[0][2][0]
    else:
        winner = max_d[0]
        parent(winner+1, set([winner+1]))
        if winner+1 == num_bidders or max_d[winner+1] == num_bidders:
            print max_bids[winner][0], max_bids[winner][2][0]
        else:
            second_high_bid = max_bids[max_d[winner+1]][1]
            index = bisect.bisect(max_bids[winner][2], second_high_bid)
            print max_bids[winner][0], max_bids[winner][2][index]

    for person in remove:
        if person in bids:
            max_d[people[person]] = people[person]
