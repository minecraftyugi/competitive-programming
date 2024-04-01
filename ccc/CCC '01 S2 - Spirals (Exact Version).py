t = input()
for a in range(t):
    x, y = map(int, raw_input().split())
    width = len(str(y))
    grid = [[""]*12 for _ in range(12)]
    i, j = 6, 6
    grid[i][j] = str(x)
    direction = "D"
    x += 1
    while x <= y:
        if direction == "D":
            i += 1
            if grid[i][j+1] == "":
                direction = "R"
        elif direction == "R":
            j += 1
            if grid[i-1][j] == "":
                direction = "U"
        elif direction == "U":
            i -= 1
            if grid[i][j-1] == "":
                direction = "L"
        else:
            j -= 1
            if grid[i+1][j] == "":
                direction = "D"

        grid[i][j] = str(x)
        x += 1

    ans = []
    left = 13
    right = -1
    for lst in grid:
        l = 13
        r = -1
        for i in range(12):
            if lst[i].isdigit():
                l = i
                break

        for i in range(11, -1, -1):
            if lst[i].isdigit():
                r = i + 1
                break

        if l < 13 or r > -1:
            ans.append(lst)

        left = min(left, l)
        right = max(right, r)

    for i in range(len(ans)):
        ans[i] = ans[i][left:right]

    for col in range(len(ans[0])):
        width = max([len(ans[i][col]) for i in range(len(ans))])
        for row in range(len(ans)):
            ans[row][col] = ans[row][col].rjust(width)

    for lst in ans:
        print " ".join(lst)
        
    if a != t-1:
        print ""
