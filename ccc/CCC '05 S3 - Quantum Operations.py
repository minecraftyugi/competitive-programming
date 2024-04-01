n = input()
tensor = []
graph = []
def merge(g1, g2):
    new = []
    for i in xrange(len(g1)):
        for i2 in xrange(len(g2)):
            row = []
            for j in xrange(len(g1[i])):         
                for j2 in xrange(len(g2[i2])):                   
                    row.append(g1[i][j] * g2[i2][j2])

            new.append(row)
            
    return new

for i in xrange(n):
    r, c = map(int, raw_input().split())
    if i == 0:
        for j in xrange(r):
            tensor.append(map(int, raw_input().split()))
    else:
        for j in xrange(r):
            graph.append(map(int, raw_input().split()))

        tensor = merge(tensor, graph)
        graph = []

rows = [0]*len(tensor)
cols = [0]*len(tensor[0])
min_elem = tensor[0][0]
max_elem = tensor[0][0]
for i in xrange(len(tensor)):
    for j in xrange(len(tensor[i])):
        elem = tensor[i][j]
        min_elem = min(min_elem, elem)
        max_elem = max(max_elem, elem)
        rows[i] += elem
        cols[j] += elem

print max_elem
print min_elem
print max(rows)
print min(rows)
print max(cols)
print min(cols)
