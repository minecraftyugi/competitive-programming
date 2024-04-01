name = raw_input()
if "." in name:
    lists = name.split(".")
    lists[0] = '"'+lists[0]+'"'
    lists[1] = lists[1].lower()
    print " - ".join(lists)
else:
    extension = raw_input().lower()
    print '"'+name+'"', "-", extension
