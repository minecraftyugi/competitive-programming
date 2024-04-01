word = raw_input()
check = 0
checker = ("A","B","C","D","E","F","G","J","K","L","M","P","Q","R","T","U","V","W","Y")

for i in checker:
    if i in word:
        check = 1
        break

if check == 1:
    print "NO"
else:
    print "YES"
