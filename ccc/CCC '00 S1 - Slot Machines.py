quarters = int(input())
num1 = int(input())%35
num2 = int(input())%100
num3 = int(input())%10
count = 0

while quarters != 0:
    count += 1
    quarters -= 1
    num1 += 1
    
    if num1 % 35 == 0:
        quarters += 30
        num1 = 0
    elif quarters == 0:
        break       

    count += 1
    quarters -= 1
    num2 += 1

    if num2 % 100 == 0 :
        quarters += 60
        num2 = 0
    elif quarters == 0:
        break

    count += 1
    quarters -= 1
    num3 += 1

    if num3 % 10 == 0:
        quarters += 9
        num3 = 0
    elif quarters == 0:
        break

print("Martha plays " + str(count) + " times before going broke.")
