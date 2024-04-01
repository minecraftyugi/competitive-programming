import itertools, collections
"""
num = int(raw_input())
lists = []

for i in range(num):
    number = int(raw_input())
"""
lists = [1,1,1,1,2,3,3,4,4]
thing = list(itertools.permutations([1,1,1,1,1], 5))
print len(thing)
print len(collections.Counter(thing).most_common())
#print [x for x in itertools.permutations([1,1,2], 3)]
print len(list(itertools.permutations(lists, 9)))
