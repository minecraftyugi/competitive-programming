import string
vowels = {"a" : 0, "e": 4, "i" : 8, "o" : 14, "u" : 20}
letters = [x for x in string.ascii_lowercase]
word = raw_input()
new = []

for i in word:
    new.append(i)
    if i in vowels.keys():
        continue
    index = letters.index(i)
    if index <= 2:
        new.append("a")
    elif index <= 6:
        new.append("e")
    elif index <= 11:
        new.append("i")
    elif index <= 17:
        new.append("o")
    else:
        new.append("u")
    if i == "z":
        new.append("z")
        continue
    newLetter = letters[index + 1]
    if newLetter in vowels:
        newLetter = letters[index + 2]
    new.append(newLetter)

print "".join(new)
