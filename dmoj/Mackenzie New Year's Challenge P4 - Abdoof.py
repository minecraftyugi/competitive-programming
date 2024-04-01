import sys
words = map(lambda x: x.lower(), raw_input().split())
a = set(["ch","t","m","d","b","bd","r"])
b = set(["a","e","i","oo"])
c = set(["n","v","f"])

if len(words) < 2:
    print "invalid"
    sys.exit()
    
def valid(word, sections, sectionType):
    len1 = word[0]

    try:
        len2 = word[:2]
    except IndexError:
        len2 = word[0]

    if len1 in a:
        sectionType.append("a")
        remove = 1
    elif len2 in a:
        sectionType.append("a")
        remove = 2
    elif len1 in b:
        sectionType.append("b")
        remove = 1
    elif len2 in b:
        sectionType.append("b")
        remove = 2
    elif len1 in c:
        sectionType.append("c")
        remove = 1
    elif len2 in c:
        sectionType.append("c")
        remove = 2
    else:
        return False
    
    if len1 not in a|b and len2 not in a|b and sections == 0:
        return False

    word = word[remove:]
    sections += 1
    
    if word == "" and sectionType[-1] == "b":
        return False

    if word == "" and sections < 2:
        return False
    
    if word != "" and sectionType[-1] == "c":
        return False

    if word == "":
        return True
    
    return valid(word, sections, sectionType)

if all(valid(word, 0, []) for word in words):
    print "valid"
else:
    print "invalid"
