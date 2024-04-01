num = int(raw_input())
punc = ["'",'"',"(",")","[","]","{","}",":",",","-","!",".","?",";","/","$","@","%","^","&","*","<",">","|"]

for i in range(num):
    line = raw_input()
    line2 = line.split()
    new = []
    sentence = ""
    for string in line2:
        line = line.replace(string, "=", 1)
    spaces = line.split("=")
    
    for word in line2:
        start = 0
        end = 0
        newWord = []
        indexes = [0] + [x for x in xrange(len(word)) if word[x] in punc] + [len(word)]

        if len(indexes) == 2:
            if indexes[1] - indexes[0] == 4:
                new.append("****")
            else:
                new.append(word)
            continue

        if indexes[1] - indexes[0] == 4:
            newWord.append("****"+word[indexes[1]])
        else:
            newWord.append(word[:indexes[1]+1])

        indexes[1] += 1

        for j in xrange(1, len(indexes) - 1):

            if indexes[j + 1] - indexes[j] == 4:
                try:
                    newWord.append("****"+word[indexes[j+1]])
                except IndexError:
                    newWord.append("****")
            else:
                if indexes[j] <= indexes[j+1]:
                    newWord.append(word[indexes[j]:indexes[j+1]+1])
            indexes[j+1] += 1

        new.append("".join(newWord))
        
    for j in xrange(len(new)):
        sentence += spaces[j] + new[j]

    sentence += spaces[-1]
    print sentence
