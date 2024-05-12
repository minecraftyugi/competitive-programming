f = open("0022_names.txt")
names = f.read().strip().replace('"', "").split(",")
names.sort()

def get_name_value(name):
    value = 0
    for ch in name:
        value += ord(ch) - 64

    return value

total = 0
for i in range(len(names)):
    total += (i+1) * get_name_value(names[i])

print(total)
