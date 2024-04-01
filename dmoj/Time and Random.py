import time, random
start_time = time.clock()
lists = []

for i in xrange(1000000):
    lists.append(random.randrange(0, 5))


#sorted(lists)
#print str(max(lists)) + " " + str(lists.count(max(lists)))
print("--- %s seconds ---" % (time.clock() - start_time))
