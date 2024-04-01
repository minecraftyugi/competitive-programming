import sys
raw_input = sys.stdin.readline

c = int(raw_input())
parents = [0]
nextParent = [0]
dict1 = {chr(a):a-96 for a in xrange(97, 123)}
ans = [0 for i in xrange(c+1)]
count = 0
positions = {}

for i in xrange(1,c+1):
    #gets the parent and next index for all indexes
    number = i
    num = len(str(bin(number)))-2
    compl = abs(number - (1 << num))
    and1 = number & compl
    parent = number - and1
    parents.append(parent)
    parent2 = number + and1
    nextParent.append(parent2)
    
for i in xrange(c):
    line = raw_input().split()
    if line[0] == "A":
        rock = line[1]
        total = 0
        for letter in rock:
            total += dict1[letter]
        
        if rock not in positions:
            count += 1
            positions[rock] = count
            ans[count] += total
            number1 = count
            
            while 1:
                update = nextParent[number1]
                if update <= c+1:
                    ans[update] += total
                    number1 = update
                else:
                    break
                
        else:
            print "Can't add", rock

    if line[0] == "S":
        rock1 = line[1]
        rock2 = line[2]
        pos1 = positions[rock1]
        pos2 = positions[rock2]
        total1 = 0
        total2 = 0
        for letter in rock1:
            total1 += dict1[letter]

        for letter in rock2:
            total2 += dict1[letter]

        difference = total2 - total1
        ans[pos1] += difference
        number = pos1
        while 1:
            update = nextParent[number]
            if update <= c+1:
                ans[update] += difference
                number = update
            else:
                break

        difference = total1 - total2
        ans[pos2] += difference
        number = pos2
        while 1:
            update = nextParent[number]
            if update <= c+1:
                ans[update] += difference
                number = update
            else:
                break

        positions[rock1], positions[rock2] = positions[rock2], positions[rock1]

    if line[0] == "M":
        rock1 = line[1]
        rock2 = line[2]
        if positions[rock2] < positions[rock1]:
            rock1, rock2 = rock2, rock1
            
        start = positions[rock1] - 1
        end = positions[rock2] 
        index1 = ans[start]
        index2 = ans[end]

        while 1:
            index1 += ans[parents[start]]
            index2 += ans[parents[end]]
            start = parents[start]
            end = parents[end]
            if start == 0 and end == 0:
                break
        print index2 - index1
        
    if line[0] == "R":
        rock1 = line[1]
        rock2 = line[2]
        total1 = 0
        total2 = 0
        pos1 = positions[rock1]
        for letter in rock1:
            total1 += dict1[letter]

        for letter in rock2:
            total2 += dict1[letter]

        difference = total2 - total1
        ans[pos1] += difference
        number = pos1
        while 1:
            update = nextParent[number]
            if update <= c+1:
                ans[update] += difference
                number = update
            else:
                break

        positions[rock2] = positions[rock1]
        del positions[rock1]
        

    if line[0] == "N":
        print count
