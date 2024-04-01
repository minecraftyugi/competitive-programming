n = input()
for i in xrange(n):
    s1, s2, s3 = raw_input(), raw_input(), raw_input()
    words = sorted([s1, s2, s3])
    words2 = sorted([s1[::-1], s2[::-1], s3[::-1]])
    if words[1].startswith(words[0]) or words[2].startswith(words[1]) or \
       words2[1].startswith(words2[0]) or words2[2].startswith(words2[1]):
        print "No"
    else:
        print "Yes"
