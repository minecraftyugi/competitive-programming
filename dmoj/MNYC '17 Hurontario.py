a, b = raw_input().split()
new_s = b + "$" + a
def prefix(s):
    pre = [0]*len(s)
    border = 0
    for i in xrange(1, len(s)):
        while border > 0 and s[i] != s[border]:
            border = pre[border-1]

        if s[i] == s[border]:
            border += 1
        else:
            border = 0

        pre[i] = border
        
    return pre

pos = prefix(new_s)[-1]
print a + b[pos:]
