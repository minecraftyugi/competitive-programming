import sys

raw_input = sys.stdin.readline
#f = open("DATA11.txt")
#raw_input = f.readline
def len_of_palindrome(s, index, offset):
    """ (str, int, int, int) -> int

    Return the length of the longest palindrome centred at index in s. The
    substring from index - offset to index + offset is a palindrome.
    Precondition: index is a valid index of s, offset is >= 0

    >>> word = "anagram"
    >>> len_of_palindrome(word, 1, 0)
    3
    >>> len_of_palindrome("radar", 3, 0)
    1
    >>> len_of_palindrome("racecar", 3, 3)
    7
    """

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
    """ (str, str) -> str

    Return a new string that starts with sep, has all characters in s separated
    by sep, and ends with sep.
    Precondition: s is even-lengthed and made up of lowercase letters

    >>> transform("hi", "$")
    '$h$i$'
    >>> transform("ecoo", "|")
    '|e|c|o|o|'
    """

    new_s = sep
    new_s += sep.join(s)
    return new_s + sep

for i in xrange(10):
    word = raw_input().strip()
    transformed = False #stores whether word has been modified
    if len(word) % 2 == 0:
        word = transform(word, "$") #make even-lengthed word odd-lengthed
        transformed = True
        
    pal_len = [0]*(len(word)+1)#lengths of palindromes centred at specific index
    longest = 0 #longest palindrome that either starts at front or ends at back
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

    if transformed:
        print len(word) / 2 - longest / 2
    else:
        print len(word) - longest
            
