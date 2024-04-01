import bisect
n = input()
list1 = raw_input().split()
m = input()
list2 = raw_input().split()
maximum = 0
test = 0
dict1 = {}
dict2 = {}
list3 = []
indexes = []
numbers = []

for index, number in enumerate(list1):
    dict1[number] = index

for index, number in enumerate(list2):
    dict2[number] = index

if n < m:
    for i in xrange(n):
        if list1[i] in dict2:
            test = 1
            num = dict2[list1[i]]
            list3.append(num)
            
            if len(list3) == 1:
                indexes.append(i)
                numbers.append(num)
            elif num > numbers[-1]:
                indexes.append(i)
                numbers.append(num)
                maximum += 1
            elif num < numbers[0]:
                indexes[0] = i
                numbers[0] = num
            else:
                index = bisect.bisect_right(numbers, num)
                indexes[index] = i
                numbers[index] = num

else:
    for i in xrange(m):
        if list2[i] in dict1:
            test = 1
            num = dict1[list2[i]]
            list3.append(num)
            
            if len(list3) == 1:
                indexes.append(i)
                numbers.append(num)
            elif num > numbers[-1]:
                indexes.append(i)
                numbers.append(num)
                maximum += 1
            elif num < numbers[0]:
                indexes[0] = i
                numbers[0] = num
            else:
                index = bisect.bisect_right(numbers, num)
                indexes[index] = i
                numbers[index] = num

print maximum + 1 if test else 0
