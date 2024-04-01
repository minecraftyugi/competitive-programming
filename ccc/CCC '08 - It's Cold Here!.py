word = ["a", "a"]
city = []
temp = []

while word[0] != "Waterloo":
    word = raw_input()
    word = word.split(" ")
    city.append(word[0])
    temp.append(word[1])
    if word[0] == "Waterloo":
        break

temp = map(int, temp)
low = temp.index(min(temp))
print city[low]
