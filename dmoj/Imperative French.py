import sys, os
try:
    #num = 50
    num = int(raw_input())
    order = { 1 : ("le", "la", "l'", "les"),
              2 : ("me", "m'", "te", "t'", "nous", "vous", "lui", "leur"),
              3 : ("y"),
              4 : ("en")
            }

    def vowelTest(vowel):
        check = "no"
        if vowel[0] == "a" or vowel[0] == "e" or vowel[0] == "i" or vowel[0] == "o" or vowel[0] == "u" or vowel[0] == "y":
            check = "yes"
        return check

    #f = open("Imperative French List.py", "r")

    for i in xrange(num):
        #line = f.readline()
        line = raw_input()
        #print line
        line = line.split()
        #line.pop(0)
        lineLen = len(line)
        word = []
        ans = []
        chop = "no"
        if line[1] == "Tu" and line[0][len(line[0]) - 3: len(line[0]) - 1] == "er" and line[lineLen - 1][len(line[lineLen - 1]) - 2] == "s":
            chop = "yes"
        for j in xrange(2, lineLen):
            string = line[j]
            if "'" in string:
                line.insert(j, string[0:2])
                line.insert(j + 1, string[2:len(string)])
                line.pop(j + 2)
        lineLen = len(line)  
        for j in xrange(2, lineLen):
            for k in xrange(1, 5):
                if line[j] in order[k]:
                    word.append(k)
        word.sort()
        for j in word:
            find = order.get(j)
            for k in xrange(2, lineLen):
                if line[k] in find and line[k] not in ans:
                    ans.append(line[k])
                    break
                else:
                    continue
        if chop == "no":
            ans.insert(0, line[lineLen - 1][0].upper() + line[lineLen - 1][1:len(line[lineLen - 1]) - 1])
        else:
            ans.insert(0, line[lineLen - 1][0].upper() + line[lineLen - 1][1:len(line[lineLen - 1]) - 2]) 
        for j in xrange(1, len(ans)):
            if ans[j] == "m'" or ans[j] == "me":
                ans.insert(j, "moi")
                ans.pop(j + 1)
                continue
            if ans[j] == "t'" or ans[j] == "te":
                ans.insert(j, "toi")
                ans.pop(j + 1)
                continue
            if ans[j] == "l'":
                ans.insert(j, "le")
                ans.pop(j + 1)
                continue
        for j in xrange(2, len(ans)):
            if j == len(ans):
                break
            if vowelTest(ans[j]) == "yes":
                if ans[j - 1] == "moi": 
                    wordList = ("m'", ans[j])
                    ans.insert(j - 1, "".join(wordList))
                    ans.pop(j)
                    ans.pop(j)
                if ans[j - 1] == "toi":
                    wordList = ("t'", ans[j])
                    ans.insert(j - 1, "".join(wordList))
                    ans.pop(j)
                    ans.pop(j)
                if ans[j - 1] == "le":
                    wordList = ("l'", ans[j])
                    ans.insert(j - 1, "".join(wordList))
                    ans.pop(j)
                    ans.pop(j)
        if len(ans) > 1:
            if line[0][len(line[0]) - 3: len(line[0]) - 1] == "er" and vowelTest(ans[1]) == "yes":
                ans.insert(0, ans[0] + "s")
                ans.pop(1)
        ans.insert(len(ans) - 1, ans[len(ans) - 1] + " !")
        ans.pop(len(ans) - 1)
        print "-".join(ans)   
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
