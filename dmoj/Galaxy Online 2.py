lists = [("CC",361),
         ("PP", 364),
         ("fear", 368),
         ("EE", 410),
         ("QOB", 387),
         ("HOL", 461),
         ("DFA", 366),
         ("HH", 413),
         ("FR", 362),
         ("LL", 367),
         ("rav", 367),
         ("TW", 361),
         ("SS", 422),
         ("LaD", 415),
         ("Rex", 510)]

lists.sort(key = lambda x: x[1], reverse = True)
print lists

order = ["TW","SS","EE","QOB","DFA","CC","RAV","REX",
         "HOL","LAD","HH","FR","PP","FEAR","LL"]
