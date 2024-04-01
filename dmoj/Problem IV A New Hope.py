num = int(raw_input())
sentence = "A long time ago in a galaxy far away...".split()

for i in xrange(num-1):
    sentence.insert(7, "far,")

print " ".join(sentence)
