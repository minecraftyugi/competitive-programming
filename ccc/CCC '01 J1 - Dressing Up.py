h = input()
lists = []

for i in xrange(1, h/2 + 1):
    spaces = " "*(2*h - (4*i-2))
    lists.append("*"*(2*i-1) + spaces + "*"*(2*i-1))

print "\n".join(lists)
print "*"*h*2
print "\n".join(lists[::-1])
