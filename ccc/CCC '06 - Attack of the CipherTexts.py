plain = raw_input()
code = raw_input()
msg = raw_input()
decode = []
#plain = list(plain)
#code = list(code)
#msg = list(msg)

for i in xrange(len(msg)):
    if code.find(msg[i]) != -1:
        find = code.find(msg[i])
        decode.append(plain[find])
    else:
        decode.append(".")

print "".join(decode)
