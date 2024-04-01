def main1():
    for i in xrange(10):
        n = input()
        numbers = map(int, raw_input().split())
        dict1 = {}
        thing = 0
        ans = 0

        for i in xrange(n):
            num = numbers[i]
            dict1[num] = i

        for i in xrange(n-1, 0, -1):
            larger = dict1[i+1]
            smaller = dict1[i]
            
            if larger < smaller:
                thing = i
                break

        if thing == 0:
            print 0
        else:
            for j in xrange(thing, 0, -1):
                num = dict1[j]
                ans += num
                
                dict1[j] = 0
                for point in dict1:
                    if dict1[point] < num:
                        dict1[point] += 1

            print ans

def main2():
    for i in xrange(10):
        n = input()
        stack = map(int, raw_input().split())
        stack.reverse()
        stack2 = []
        ans = 0
        maximum = 0
        minimum = 1
        car = stack.pop()
        while len(stack) != 0:
            stack2.append(car)
            if car > maximum:
                maximum = car
            elif car > minimum:
                minimum = car
            car = stack.pop()

        if car > maximum:
            maximum = car
        elif car > minimum:
            minimum = car
          
        stack2.append(car)
        while len(stack2) != 0:
            stack.append(stack2.pop())
            
        while minimum != 0:
            car = stack.pop()
            while car != minimum:
                stack2.append(car)
                ans += 1
                car = stack.pop()

            while len(stack2) != 0:
                stack.append(stack2.pop())

            stack.append(car)
            minimum -= 1

        print ans

parent = [0]*1001
child = [0]*1001
for i in range(1001):
    compl = i & -i
    parent[i] = i - compl
    child[i] = i + compl

def bit_add(index, tree):
    while index > 0:
        tree[index] += 1
        index = parent[index]
        
    return

def bit_sum(index, tree):
    ans = 0
    while index < 1001:
        ans += tree[index]
        index = child[index]
        
    return ans

def main3():
    for i in xrange(10):
        n = input()
        stack = map(int, raw_input().split())
        ans = 0
        maximum = 0
        minimum = 1
        for car in stack:
            if car > maximum:
                maximum = car
            elif car > minimum:
                minimum = car
                
        tree = [0]*1001
        distances = {}
        for i in range(n):
            distances[stack[i]] = i + 1

        for i in range(minimum, 0, -1):
            ans += distances[i] + bit_sum(distances[i], tree) - 1
            bit_add(distances[i] - 1, tree)

        print ans

#main1()
#main2()
main3()
