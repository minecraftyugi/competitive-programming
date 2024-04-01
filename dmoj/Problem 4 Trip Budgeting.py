lines = map(int, raw_input().split())
excite = lines[0]
transport = lines[1]
hotel = lines[2]
food = lines[3]
num = int(raw_input())
dict1 = {}

for i in range(num):
    thing = map(int, raw_input().split())
    excitement = thing[0]
    cost = thing[1] - thing[-1]
    hotel2 = thing[2]
    if hotel2 > hotel:
        total = cost + hotel2
    else:
        total = cost + hotel
    dict1[i+1] = [excitement, cost, hotel2, total]

print dict1

sums = [(dict1[x][3], x) for x in dict1.keys()]
sums.sort(key = lambda x: (x[0], dict1[x[1]][1]))
print sums

def best(index, graph, cost, maxHotel, exciteLevel):    
    #print index, cost, maxHotel, exciteLevel
    index += 1
    newCost = cost
    newHotel = graph[sums[index][1]][2]

    if newHotel > maxHotel:
        newCost -= maxHotel
        maxHotel = newHotel
        newCost += newHotel

    newCost += graph[sums[index][1]][1]
    #print "Newcost", newCost, "Cost", cost
    exciteLevel += graph[sums[index][1]][0]
    if newCost <= cost:
        return best(index, graph, newCost, maxHotel, exciteLevel)
    if exciteLevel < excite:
        return best(index, graph, newCost, maxHotel, exciteLevel)
    return cost

maxHotel = max(hotel, dict1[sums[0][1]][2])
print best(0, dict1, sums[0][0], maxHotel, dict1[sums[0][1]][0]) + transport + food
