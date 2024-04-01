num1 = int(raw_input())
num2 = int(raw_input())
num3 = num1 - num2
count = 2

while num2 <= num1 and num3 >= 0:
    num3 = num1 - num2
    num1 = num2
    num2 = num3
    count += 1

print count
