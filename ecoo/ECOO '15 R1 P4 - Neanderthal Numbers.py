for i in xrange(10):
    word = raw_input()
    ans = [0]*(len(word) + 1)
    ans[0] = 1
    
    for index, letter in enumerate(word):
        if index < 1:
            continue

        if word[index - 1: index + 1] == "ug":
            ans[index+1] += ans[index - 1]

        if index < 2:
            continue

        if word[index - 2: index + 1] in set(["ook", "oog"]):
            ans[index+1] += ans[index - 2]

        if index < 3:
            continue

        if word[index - 3: index + 1] in set(["ooga", "mook", "ugug"]):
            ans[index+1] += ans[index - 3]

        if index < 4:
            continue

        if word[index - 4: index + 1] in set(["oogam", "oogum"]):
            ans[index+1] += ans[index - 4]

        if index < 5:
            continue

        if word[index - 5: index + 1] == "ookook":
            ans[index+1] += ans[index - 5]

        if index < 7:
            continue

        if word[index - 7: index + 1] == "mookmook":
            ans[index+1] += ans[index - 7]

    print ans[-1]
