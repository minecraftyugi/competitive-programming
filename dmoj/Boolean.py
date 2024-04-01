string = raw_input()

lists = string.split(" ")
count = lists.count('not')
lists = "".join(lists)
true = lists.find("True")
false = lists.find("False")
if true != -1:
    if count % 2 == 0:
        print "True"
    else:
        print "False"
if false != -1:
    if count % 2 == 0:
        print "False"
    else:
        print "True"
