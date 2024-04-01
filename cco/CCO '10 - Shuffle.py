letters = [0]*27
loop = [0]*27
for i in xrange(27):
    letter = ord(raw_input()) - 65
    if letter == 30:
        letter = 26

    letters[i] = letter

for i in xrange(27):
    if not loop[i]:
        visited = [0]*27
        visited[i] = 1
        count = 1
        start = letters[i]
        while not visited[start]:
            count += 1
            visited[start] = 1
            start = letters[start]

        for j in xrange(27):
            if visited[j]:
                loop[j] = count
                
n = input()
word = raw_input()
ans = ""
for ch in word:
    if ch == "_":
        ch = 26
    else:
        ch = ord(ch) - 65

    dist = n % loop[ch]
    index = 0
    while index < dist:
        ch = letters[ch]
        index += 1

    if ch == 26:
        ans += "_"
    else:
        ans += chr(ch + 65)

print ans
