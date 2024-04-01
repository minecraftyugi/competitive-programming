num1 = ""
num2 = ""
playlist = ['A','B','C','D','E']

while (num1 != "4" and num2 != "1"):
    num1 = int(raw_input())
    num2 = int(raw_input())
    if (num1 == 4 and num2 == 1):
        print " ".join(playlist)
        break
    for i in xrange(num2):
        if num1 == 1:
            playlist.append(playlist[0])
            playlist.pop(0)
        if num1 == 2:
            playlist.insert(0, playlist[4])
            playlist.pop(5)
        if num1 == 3:
            playlist.insert(0, playlist[1])
            playlist.pop(2)
        if num1 == 4:
            print " ".join(playlist)
