import sys, string

raw_input = sys.stdin.readline
alphabet = string.ascii_lowercase
#f = open("DATA21.TXT", "r")
#raw_input = f.readline

for i in xrange(10):
    k = int(raw_input().strip()) % 26
    msg = raw_input().strip()
    if " " in msg:
        word_list = msg.split()
        length = len(word_list)
        first_letter = alphabet[length / 26]
        length %= 26
        second_letter = alphabet[length]
        code = first_letter + second_letter #stores the encoding
        for word in word_list:
            code += alphabet[len(word)]

        total_msg = code + "".join(word_list)
        final_str = "" #stores a reverse of the message to be printed
        for j in xrange(len(total_msg) - 1, -1, -1):
            position = alphabet.index(total_msg[j]) + k
            position %= 26
            final_str += alphabet[position]
            k = position

        print final_str[::-1]
        
    else:
        total_msg = "" #stores a reverse of the original message with encoding
        for j in xrange(len(msg) - 1, -1, -1):
            position = alphabet.index(msg[j]) - k
            position %= 26
            total_msg += alphabet[position]
            k += position

        final_str = total_msg[::-1]
        num_words = alphabet.index(final_str[0]) * 26
        num_words += alphabet.index(final_str[1])
        word_list = []
        left_pos = 2 + num_words #offset due to encoding at front
        right_pos = 2 + num_words #offset due to encoding at front
        for j in xrange(2, num_words + 2):
            word_length = alphabet.index(final_str[j])
            right_pos += word_length
            word_list.append(final_str[left_pos : right_pos])
            left_pos = right_pos

        print " ".join(word_list)
