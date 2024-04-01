s1 = raw_input()
s2 = raw_input()
alpha1 = [0]*26
alpha2 = [0]*26
for ch in s1:
    if not ch.isspace():
        alpha1[ord(ch) - ord("A")] += 1

for ch in s2:
    if not ch.isspace():
        alpha2[ord(ch) - ord("A")] += 1

if alpha1 == alpha2:
    print "Is an anagram."
else:
    print "Is not an anagram."
