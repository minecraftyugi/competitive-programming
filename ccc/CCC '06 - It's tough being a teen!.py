import sys

dict1 = {1 : [4,7], 2 : [1], 3 : [4,5], 4 : [], 5 : [], 6 : [], 7 : []}
lists0 = []

while 1:
    num1 = int(raw_input())
    num2 = int(raw_input())
    if num1 == 0 and num2 == 0:
        break
    else:
        dict1[num1].append(num2)
        dict1[num1].sort()

def verify(start, end, graph):
    new = []
    if start in end:
        return "NO"
    for i in end:
        try:
            numbers = graph[i]
            for j in numbers:
                new.append(j)
        except KeyError:
            pass

    new = sorted(set(new))
    if new == []:
        return "YES"
    else:
        return verify(start, new, graph)
    
def order(lists, graph):
    for i in graph.keys():
        check = [x for x in graph.keys() if i in graph[x]]
        if check == []:
            lists.append(i)
            del graph[i]
            return order(lists, graph)
            break
        
    if len(lists) == 7:
        return " ".join(map(str, lists))
    return order(lists, graph)

for i in xrange(1, 8):
    check = verify(i, dict1[i], dict1)
    if check == "NO":
        print "Cannot complete these tasks. Going to bed."
        sys.exit()

for i in xrange(1, 8):
    check = [x for x in dict1.keys() if i in dict1[x]]
    if check == []:
        lists0.append(i)
        del dict1[i]
        break
    
print order(lists0, dict1)
