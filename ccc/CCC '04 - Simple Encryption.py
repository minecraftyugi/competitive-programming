import math
code = raw_input()
word = raw_input()
lists = []
ans = []
test = []
index = 0
letters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

for i in xrange(len(word)):
    if word[i] in letters:
        lists.append(word[i])

for i in xrange(len(code)):
    test.append(letters.index(code[i]))
      
for i in xrange(int(math.ceil(len(lists) / float(len(code))))):
    for j in xrange(len(code)):
        if index == len(lists):
            break
        if test[j] + letters.index(lists[index]) < 26:
            ans.append(letters[test[j] + letters.index(lists[index])])
        else:
            ans.append(letters[test[j] + letters.index(lists[index]) - 26])
        index += 1

print "".join(ans)
