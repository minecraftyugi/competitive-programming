num = int(raw_input())

for i in xrange(num):
    phone = raw_input()
    phone = phone.split("-")
    phone = "".join(phone)
    phone = list(phone)
    for j in xrange(len(phone)):
        if phone[j] == "A" or phone[j] == "B" or phone[j] == "C":
            phone[j] = "2"
        if phone[j] == "D" or phone[j] == "E" or phone[j] == "F":
            phone[j] = "3"
        if phone[j] == "G" or phone[j] == "H" or phone[j] == "I":
            phone[j] = "4"
        if phone[j] == "J" or phone[j] == "K" or phone[j] == "L":
            phone[j] = "5"
        if phone[j] == "M" or phone[j] == "N" or phone[j] == "O":
            phone[j] = "6"
        if phone[j] == "P" or phone[j] == "Q" or phone[j] == "R" or phone[j] == "S":
            phone[j] = "7"
        if phone[j] == "T" or phone[j] == "U" or phone[j] == "V":
            phone[j] = "8"
        if phone[j] == "W" or phone[j] == "X" or phone[j] == "Y" or phone[j] == "Z":
            phone[j] = "9"
    phone.insert(3, '-')
    phone.insert(7, '-')
    if len(phone) > 12:
        for i in xrange(len(phone), 12, -1):
            phone.pop(i - 1) 
    phone = "".join(phone)
    print phone

