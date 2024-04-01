line = ""
A = 0
B = 0

while line != "7":
    line = raw_input()
    if line == "7":
        break
    line = line.split(" ")
    if line[0] == "1":
        if line[1] == "A":
            A = int(line[2])
        if line[1] == "B":
            B = int(line[2])
    if line[0] == "2":
        if line[1] == "A":
            print A
        if line[1] == "B":
            print B        
    if line[0] == "3":
        if line[1] == "A" and line[2] == "B":
            A = A + B
        if line[1] == "B" and line[2] == "A":
            B = B + A
        if line[1] == "A" and line[2] == "A":
            A = A + A
        if line[1] == "B" and line[2] == "B":
            B = B + B
    if line[0] == "4":
        if line[1] == "A" and line[2] == "B":
            A = A * B
        if line[1] == "B" and line[2] == "A":
            B = B * A
        if line[1] == "A" and line[2] == "A":
            A = A * A
        if line[1] == "B" and line[2] == "B":
            B = B * B
    if line[0] == "5":
        if line[1] == "A" and line[2] == "B":
            A = A - B
        if line[1] == "B" and line[2] == "A":
            B = B - A
        if line[1] == "A" and line[2] == "A":
            A = A - A
        if line[1] == "B" and line[2] == "B":
            B = B - B
    if line[0] == "6":
        if line[1] == "A" and line[2] == "B":
            A = A / B
        if line[1] == "B" and line[2] == "A":
            B = B / A
        if line[1] == "A" and line[2] == "A":
            A = A / A
        if line[1] == "B" and line[2] == "B":
            B = B / B
