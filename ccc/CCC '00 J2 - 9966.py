from math import *
m = int(input())
n = int(input())

rotate = ["0","1","8"]
thing = ["6","9"]
count = 0

for i in range(m, n+1):
    test = 1
    num = str(i)
    
    for j in ["2","3","4","5","7"]:
        if j in num:
            test = 0
            break

    for j in range(ceil(len(num)/2)):
        if j == ceil(len(num)/2):
            if num[j] not in rotate:
                test = 0
                break
        else:
            if num[j] == "6" and num[-(j+1)] != "9":
                test = 0
                break
            elif num[j] == "9" and num[-(j+1)] != "6":
                test = 0
                break
            elif num[j] == "0" and num[-(j+1)] != "0":
                test = 0
                break
            elif num[j] == "1" and num[-(j+1)] != "1":
                test = 0
                break
            elif num[j] == "8" and num[-(j+1)] != "8":
                test = 0
                break
                
    if test == 0:
        continue

    count += 1

print(count)
