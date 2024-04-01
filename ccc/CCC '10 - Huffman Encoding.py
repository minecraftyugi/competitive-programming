num = int(raw_input())
decode = {}
ans = []

for  i in xrange(num):
    code = raw_input()
    code = code.split()
    decode.update({code[1] : code[0]})

binary = raw_input()
j = 0
for i in range(len(binary) + 1):
    if binary[j:i] in decode:
        ltr = binary[j:i]
        ans.append(decode[ltr])
        j = i
print "".join(ans)
