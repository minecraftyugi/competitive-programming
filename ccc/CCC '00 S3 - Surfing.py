from HTMLParser import HTMLParser
import collections

class newParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    print "Link from", url, "to", attr[1]
                    dict1[url].add(attr[1])

def paths(starts, end, graph, visited):
    new = set()

    for start in starts:
        neighbours = graph[start]

        for neighbour in neighbours:
            if neighbour == end:
                return True
            if neighbour not in visited:
                new.add(neighbour)
                visited.add(neighbour)

    if len(new) == 0:
        return False
    
    return paths(new, end, graph, visited)

n = input()
dict1 = collections.defaultdict(set)
parser = newParser()

for i in xrange(n):
    url = raw_input()
    body = ""

    while 1:
        string = raw_input()
        body += string
        
        if string == "</HTML>":
            break
    
    parser.feed(body)
    parser.reset()
    parser.close()

parser.close()

while 1:
    str1 = raw_input()

    if str1 == "The End":
        break
    else:
        str2 = raw_input()
        result = paths([str1], str2, dict1, set([str1]))

        if result is True:
            print "Can surf from", str1, "to", str2 + "."
        else:
            print "Can't surf from", str1, "to", str2 + "."
