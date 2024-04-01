adjective = int(raw_input())
noun = int(raw_input())
adjList = []
nounList = []

for i in xrange(adjective):
    word = raw_input()
    adjList.append(word)
for i in xrange(noun):
    word = raw_input()
    nounList.append(word)

for i in xrange(len(adjList)):
    for j in xrange(len(nounList)):
        print adjList[i] + " as " + nounList[j]
