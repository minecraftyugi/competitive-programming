day,num = list(map(int,input().split()))
days = "Sun Mon Tue Wed Thr Fri Sat".split()

print(" ".join(days))
current = ""

for i in range(1, day):
    current += " "*4
    
for i in range(1, num+1):
    current += " "*(3-len(str(i))) + str(i) + " "

    if (day+i)%7 == 1:
        print(current.rstrip())
        current = ""

if current != "":
    print(current.rstrip())
