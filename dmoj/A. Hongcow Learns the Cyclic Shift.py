word = raw_input()
ans = set([word])
new_word = word

for i in xrange(len(word)):
    new_word = new_word[-1] + new_word[:-1]
    ans.add(new_word)

print len(ans)
