eq = raw_input()
eq = eq.split()
ans = 0

for i in range(len(eq) - 1):
    if i == 0:
        ans += int(eq[i])
    if eq[i] == "P":
        ans += int(eq[i + 1])
    elif eq[i] == "M":
        ans -= int(eq[i + 1])
    else:
        pass

print ans
