dist, buildings, roads, stores = map(int, raw_input().split())

storeList = []
dict1 = {}
dict2 = {}

for i in range(stores):
    storeList.append(int(raw_input()))

for i in range(roads):
    placeA, placeB, length = map(int, raw_input().split())

    if placeA not in dict1:
        dict1.update({placeA : [(placeB, length)]})
    else:
        tuples = dict1[placeA]
        
        for i in tuples:
            if i[0] == placeB:
                if i[1] > length:
                    tuples.pop(tuples.index(i))
                    
        tuples.append((placeB, length))
        dict1.update({placeA : tuples})

for i in dict1[0]:
    dict2.update({ i[0] : i[1]})

def paths(startDict, end, graph):
    global storeList
    delpaths = []
    dict3 = {}
    
    if end == []:
        return
    
    for i in startDict.keys():
        if startDict[i] >= dist:
            delpaths.append(i)
        else:
            if i in end:
                storeList.pop(storeList.index(i))
    
    for i in delpaths:
        del startDict[i]      
    
    for i in startDict.keys():
        try:
            new = graph[i]
            for value in new:
                if value[0] not in dict3:
                    dict3.update({ value[0] : [startDict[i] + value[1]] })
                else:
                    already = dict3[value[0]]
                    already.append(startDict[i] + value[1])
                    dict3.update({ value[0] : already })
                    
        except KeyError:
            pass
    
    for i in dict3.keys():
        dict3.update({ i : min(dict3[i])})
        
    if dict3 == {}:
        return
    
    paths(dict3, end, graph)
    return

paths(dict2, storeList, dict1)
print stores - len(storeList)
