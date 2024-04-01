def solve(word):
    stack = []
    valid = "ABNS"
    l1 = ["B","A","S"]
    l2 = ["A","N","A"]
    for ch in word:
        if ch not in valid:
            return "NO"

        stack.append(ch)           
        if len(stack) < 3:
            if ch == "S":
                return "NO"
        else:
            changed = True
            while ch in "AS" and changed:
                if ch == "S":
                    if stack[-3:] == l1:
                        stack.pop() and stack.pop() and stack.pop()
                        stack.append("A")
                    else:
                        return "NO"
                elif ch == "A":
                    if stack[-3:] == l2:
                        stack.pop() and stack.pop() and stack.pop()
                        stack.append("A")
                    else:
                        changed = False
                else:
                    changed = False

                ch = stack[-1]
    
    return ["NO", "YES"][stack == ["A"]]

word = raw_input()
while word != "X":
    print solve(word)
    word = raw_input()
