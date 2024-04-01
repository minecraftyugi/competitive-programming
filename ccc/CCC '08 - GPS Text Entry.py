word = raw_input()

keypad = [
    ['A','B','C','D','E','F'],
    ['G','H','I','J','K','L'],
    ['M','N','O','P','Q','R'],
    ['S','T','U','V','W','X'],
    ['Y','Z',' ','-','.','ENTER']]

moves = 0
oldPos = [0,0]
newPos = [0,0]

for letter in list(word):
    for i in range(5):
        if letter in keypad[i]:
            oldPos = newPos
            newPos = [i, keypad[i].index(letter)]
            moves += abs(newPos[0]-oldPos[0]) + abs(newPos[1]-oldPos[1])
            break

print moves + abs(newPos[0]-4) + abs(newPos[1]-5)
