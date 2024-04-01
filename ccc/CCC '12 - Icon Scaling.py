num = int(raw_input())

star = "*" * num
x = "x" * num
space = " " * num

for i in range(num):
    print star + x + star

for i in range(num):
    print space + x + x

for i in range(num):
    print star + space + star
