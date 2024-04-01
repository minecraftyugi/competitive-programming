length = input()
word = raw_input()
def len_of_palindrome(s, index, offset):
    start_index = 0
    end_index = len(s)
    l_index = index - offset - 1
    r_index = index + offset + 1
    valid = True
    while start_index <= l_index and r_index < end_index and valid:
        if s[l_index] == s[r_index]:
            l_index -= 1
            r_index += 1
        else:
            valid = False

    return r_index - l_index - 1

def transform(s, sep):
    new_s = sep
    new_s += sep.join(s)
    return new_s + sep

transformed = False
if len(word) % 2 == 0:
    word = transform(word, "$")
    transformed = True

length = len(word)    
pal_len = [0]*(length+1)
longest = 0 
index = 0
offset = 0
terminate = False
while index < len(word) and not terminate:
    length = len_of_palindrome(word, index, offset)
    offset = 0
    pal_len[index] = length
    boundary = length / 2
    if index + boundary == len(word) - 1:
        terminate = True

    if length > longest:
        if index - boundary == 0 or index + boundary == len(word) - 1:
            longest = length
            
    if boundary > 0 and not terminate:
        pos = 1
        new_index = False
        while pos <= boundary and not new_index:
            left_pos = index - pos - pal_len[index-pos] / 2
            if left_pos < index - boundary:
                pal_len[index+pos] = len_of_palindrome(word, index + pos, \
                                                       boundary - pos)
            elif left_pos > index - boundary:
                pal_len[index+pos] = pal_len[index-pos]
            else:
               new_index = True
               offset = pal_len[index-pos] / 2
               pos -= 1

            pos += 1

        index += pos
    else:
        index += 1

maximum = max(pal_len)
position = pal_len.index(maximum)
if transformed:
    print word[position - maximum/2:position+maximum/2].replace("$", "")
    print maximum / 2
else:
    print word[position-maximum/2:position+maximum/2+1]
    print maximum  
