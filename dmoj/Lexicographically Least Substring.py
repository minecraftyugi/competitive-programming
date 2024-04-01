def sort_characters(s):
    """ (str) -> list of int

    Return the positions of where all letters in s would be in the sorted order.
    In case there are duplicate letters in s, the letter with the lower index
    in s will have appear at a lower position in the sorted list.

    >>> sort_characters("aaa")
    [0, 1, 2]
    >>> sort_characters("cab")
    [1, 2, 0]
    >>> sort_characters("cba")
    [2, 1, 0]
    >>> sort_characters("aba")
    [0, 2, 1]
    """

    order = [0]*len(s)
    count = [0]*26
    for i in xrange(len(s)):
        count[ord(s[i])-97] += 1 #increase count of each letter in s

    for i in xrange(1, 26):
        count[i] += count[i-1] #prefix sum of smaller letters

    for i in xrange(len(s)-1, -1, -1):
        pos = ord(s[i])-97
        count[pos] -= 1 #contains postion right after all smaller letters
        order[count[pos]] = i #set position in order to the ith letter

    return order

def compute_char_classes(s, order):
    """ (str, list of int) -> list of int

    Return the equivalence classes for each position in s, given the sorted
    order of letters in s. This is the number of different cyclic shifts of
    length L that are strictly smaller than the partial cyclic shift of length
    L starting at index i.
    
    >>> compute_char_classes("ababaa$", [6,0,2,4,5,1,3])
    [1, 2, 1, 2, 1, 1, 0]
    """

    ch_class = [0]*len(s)
    for i in xrange(1, len(s)):
        if s[order[i]] != s[order[i-1]]:
            ch_class[order[i]] = ch_class[order[i-1]] + 1
        else:
            ch_class[order[i]] = ch_class[order[i-1]]

    return ch_class

def sort_doubled(s, L, order, ch_class):
    """ (str, int, list of int, list of int) -> list of int

    """

    n = len(s)
    count = [0]*n
    new_order = [0]*n
    for i in xrange(n):
        count[ch_class[i]] += 1

    for i in xrange(1, n):
        count[i] += count[i-1]

    for i in xrange(n - 1, -1, -1):
        start = (order[i] - L + n) % n
        pos = ch_class[start]
        count[pos] -= 1
        new_order[count[pos]] = start

    return new_order

def update_classes(new_order, ch_class, L):
    """ (list of int, list of int, int) -> list of int

    Return the new equivalence class for ch_class, given the sorted order of
    the string, new_order, and the length of the partial cyclic shift L.

    """

    n = len(new_order)
    new_class = [0]*n
    for i in xrange(1, n):
        curr = new_order[i]
        prev = new_order[i-1]
        mid = (curr + L) % n
        mid_prev = (prev + L) % n
        if ch_class[curr] != ch_class[prev] or \
        ch_class[mid] != ch_class[mid_prev]:
            new_class[curr] = new_class[prev] + 1

        else:
            new_class[curr] = new_class[prev]

    return new_class

def build_suffix_array(s):
    """ (str) -> list of int

    Return the suffix array for string s.

    """

    order = sort_characters(s)
    ch_class = compute_char_classes(s, order)
    L = 1
    while L < len(s):
        order = sort_doubled(s, L, order, ch_class)
        ch_class = update_classes(order, ch_class, L)
        L *= 2

    return order

def main(s, k):    
    #s = raw_input()
    #k = input()
    n = len(s)
    suffix = build_suffix_array(s)
    for i in suffix:
        if n - i >= k:
            break
            #print s[i:i+k]
            #raise SystemExit

import cProfile
cProfile.run("main('aa'*10**5, 100)")
