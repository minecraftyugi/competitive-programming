num = int(raw_input())
word = raw_input()
decode = []
tup = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

for i in range(1, len(word) + 1):
    dist = 3 * i + num
    find = tup.index(word[i - 1])
    if find - dist < 0:
        decode.append(tup[26 + find - dist])
        continue
    else:
        decode.append(tup[find - dist])

print "".join(decode)
