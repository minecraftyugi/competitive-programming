import sys
raw_input = sys.stdin.readline

word = raw_input().strip()
n = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
possible = set()

for i in xrange(len(word) - 8):
    if word[i]==word[i+4] and word[i+1]==word[i+8]:
        if len(set(list(word[i:i+9])))==7:
            new = word[i:i+9]
            possible.add(new)

for i in xrange(n):
    a = raw_input().strip()
    dict1 = {value:index for index, value in enumerate(a)}
    newWord = a[7]+a[0]+a[8]+a[11]+a[7]+a[24]+a[3]+a[17]+a[0]

    if newWord in possible:
        for letter in word:
            index = dict1[letter]
            ans += alphabet[index]

        print ans
        sys.exit()

print "KeyNotFoundError"
