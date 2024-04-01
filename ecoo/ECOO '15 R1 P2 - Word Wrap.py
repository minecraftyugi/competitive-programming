def check(currentString, add, test):
    if test == 0 and len(add) > n:
        return add[:n], add[n:], 1
    elif test == 1 and len(add) + len(currentString) + 1 > n:
        return currentString, add, 1
    elif test == 0:
        currentString = add
        return "", currentString, 0   
    else:
        currentString += " " + add
        return "", currentString, 0        

for i in xrange(10):
    n = input()
    words = raw_input().split()
    checker = 0
    string = ""
    for word in words:
        while 1:
            if n - len(string) <= 1 and checker != 0:
                print string
                string = ""
                checker = 0
                
            printer, new, boolean = check(string, word, checker)
            
            if boolean:
                print printer
                word = new
                string = ""
                checker = 0
            else:
                checker = 1
                string = new
                break

    print string
    print "="*5
