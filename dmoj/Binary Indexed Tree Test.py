#works
import sys
raw_input = sys.stdin.readline
line = map(int, raw_input().split())
n = line[0]
m = line[1]
parents = [0]
nextParent = [0]
ans = [0 for i in xrange(n+1)] #stores prefix sums
ans2 = [0 for i in xrange(100001)] #stores the amount of elements less than specified number
numbers = [0] + map(int, raw_input().split())
total = sys.stdin.read().strip().split("\n")

for i in xrange(1,100001):
    #gets the parent index for all indexes
    number = i
    num = len(str(bin(number)))-2
    compl = abs(number - (1 << num))
    and1 = number & compl
    parent = number - and1
    parents.append(parent)
    parent2 = number + and1
    nextParent.append(parent2)

for i in xrange(1,n+1):
    #updates prefix sums in nlogn
    #updates the amount of smaller numbers in nlogn
    add = numbers[i]
    ans[i] += add
    ans2[add] += 1
    number1 = i
    number2 = add
    test1, test2 = 0, 0
    while 1:
        update = nextParent[number1]
        if update <= n+1:
            ans[update] += add
            number1 = update
        else:
            test1 = 1

        update2 = nextParent[number2]
        if update2 <= 100001:
            ans2[update2] += 1
            number2 = update2
        else:
            test2 = 1

        if test1 == 1 and test2 == 1:
            break

for i in xrange(m):
    #operation = raw_input().split()
    operation = total[i].split()
    op = operation[0]
    if op == "C":
        #each change is logn
        index = int(operation[1])
        new = int(operation[2])
        old = numbers[index]
        numbers[index] = new
        difference = new - old
        ans[index] += difference
        ans2[old] -= 1
        ans2[new] += 1
        number = index
        number2 = old
        number3 = new
        test1, test2, test3 = 0, 0, 0
        while 1:
            update = nextParent[number]
            if update <= n+1:
                ans[update] += difference
                number = update
            else:
                test1 = 1

            update = nextParent[number2]
            if update <= 100001:
                ans2[update] -= 1
                number2 = update
            else:
                test2 = 1

            update = nextParent[number3]
            if update <= 100001:
                ans2[update] += 1
                number3 = update
            else:
                test3 = 1

            if test1 == 1 and test2 == 1 and test3 == 1:
                break
            
    elif op == "Q":
        #does a query in logn
        number = int(operation[1])
        index = ans2[number]
        while 1:
            index += ans2[parents[number]]
            number = parents[number]
            if number == 0:
                break
        print index
        
    else:
        #does a query in logn
        start = int(operation[1]) - 1
        end = int(operation[2])
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
