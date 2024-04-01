import sys

sys.setrecursionlimit(10000)
raw_input = sys.stdin.readline
f = open(r"C:\Users\User\Desktop\ECOOCS_2016\Round 3\DATA\DATA31.TXT", "r")
raw_input = f.readline
def solve(wordlist, special, memo):
  if special in memo:
    ans = memo[special]
  elif len(special) == 0:
    ans = 0
  else:
    ans = float('inf')
    for i in range(len(special) + 1):
      if special[:i] in wordlist:
        takes = solve(wordlist, special[i:], memo) + 1
        ans = min(ans, takes)
  memo[special] = ans
  return memo[special]

dictionary = set()
cache = {}
n = int(raw_input().strip())
for i in xrange(n):
    word = raw_input().strip()
    dictionary.add(word)

for i in xrange(10):
    word = raw_input().strip()
    print solve(dictionary, word, cache) - 1

import sys

sys.setrecursionlimit(10000)
raw_input = sys.stdin.readline
f = open(r"C:\Users\User\Desktop\ECOOCS_2016\Round 3\DATA\DATA31.TXT", "r")
raw_input = f.readline
##def split_word(s):
##    """ (str) -> int
##
##    Return the minimum amount of words in the dictionary needed to create s.
##
##    """
##
##    if s in dictionary:
##        return 1
##    else:
##        min_words = 2001 #default maximum; a word can have only 2000 characters
##        for i in xrange(1, len(s)):
##            substr1 = s[:i]
##            substr2 = s[i:]
##            if substr1 in cache:
##                amount1 = cache[substr1]
##            else:
##                amount1 = split_word(substr1)
##                cache[substr1] = amount1
##                
##            if substr2 in cache:
##                amount2 = cache[substr2]
##            else:
##                amount2 = split_word(substr2)
##                cache[substr2] = amount2
##
##            total_amount = amount1 + amount2
##            if total_amount < min_words:
##                min_words = total_amount
##
##        return min_words
##
def search(word_list, ch, pos, upper, lower):
    """ (list of str, str, int, int, int) -> tuple of (int, int)

    Return the upper and lower ranges of binary searching word_list for a
    character in s at index pos. The binary search in word_list will be done
    inbetween indexes upper and lower.
    Precondition: word_list is sorted.
    """

    if pos == len(word_list[upper]):
        upper += 1
    
    prev_upper = upper
    prev_lower = lower
    #find upper bound
    while upper < lower:
        mid = (upper + lower) / 2
        if ch <= word_list[mid][pos]:
            lower = mid
        else:
            upper = mid + 1

    #find lower bound
    while prev_upper < prev_lower:
        mid = (prev_upper + prev_lower) / 2
        if ch < word_list[mid][pos]:
            prev_lower = mid
        else:
            prev_upper = mid + 1

    return upper, prev_lower

def fill_table(word_list, s, table):
    """ (list of int, str, list of int) -> None

    Modify table so that for each index i, table[i] contains the minimum amount
    of words in word_list needed to make the substring of s starting at index 0
    and ending at index i. If it is not possible for a substring to be made at
    index i, table[i] = 0.
    Precondition: word_list is sorted.
    """

    word_len = len(s)
    for i in xrange(word_len):
        upper = 0
        lower = len(word_list)
        pos = i
        delta = 1 if i != 0 else 0
        while pos < word_len and upper < lower:
            ch = s[pos]
            new_up, new_low = search(word_list, ch, pos - i, upper, lower)
            if new_up != upper:
                if pos - i == len(word_list[upper]) and table[i]:
                    if table[pos] == 0:
                        table[pos] = table[i] + delta
                    else:
                        table[pos] = min(table[pos], table[i] + delta)

            upper = new_up
            lower = new_low
            pos += 1

        if upper < lower and table[i]:
            if table[pos] == 0:
                table[pos] = table[i] + delta
            else:
                table[pos] = min(table[pos], table[i] + delta)
            
    return

dictionary = set()
words = []
cache = {}
n = int(raw_input().strip())
for i in xrange(n):
    word = raw_input().strip()
    dictionary.add(word)
    words.append(word)

words.sort()

for i in xrange(10):
    word = raw_input().strip()
    length = len(word)
    dp = [0]*(length+1)
    dp[0] = 1
    start = time.time()
    fill_table(words, word, dp)
    print dp[length] - 1
    print time.time() - start, "seconds"
    #print split_word(word) - 1

def split_word(s, dictionary, cache):
    """ (str) -> int

    Return the minimum amount of words in the dictionary needed to create s.

    """

    if s in dictionary:
        min_words = 1
    elif s in cache:
        min_words = cache[s]
    else:
        min_words = 2001 #default maximum; a word can have only 2000 characters
        for i in xrange(1, len(s)):
            substr1 = s[:i]
            substr2 = s[i:]
            if substr1 in cache:
                amount1 = cache[substr1]
            elif substr1 in dictionary:
                amount1 = 1
            else:
                amount1 = split_word(substr1, dictionary, cache)
                cache[substr1] = amount1
                
            if substr2 in cache:
                amount2 = cache[substr2]
            elif substr2 in dictionary:
                amount2 = 1
            else:
                amount2 = split_word(substr2, dictionary, cache)
                cache[substr2] = amount2

            total_amount = amount1 + amount2
            min_words = min(min_words, total_amount)

    cache[s] = min_words
    return min_words

def solve(wordlist, special, memo):
  if special in memo:
    ans = memo[special]
  elif len(special) == 0:
    ans = 0
  else:
    ans = float('inf')
    for i in range(len(special) + 1):
      if special[:i] in wordlist:
        takes = solve(wordlist, special[i:], memo) + 1
        ans = min(ans, takes)
  memo[special] = ans
  return memo[special]

dictionary = set()
cache = {}
n = int(raw_input().strip())
for i in xrange(n):
    word = raw_input().strip()
    dictionary.add(word)

for i in xrange(10):
    word = raw_input().strip()
    #print solve(dictionary, word, cache) - 1
    #print split_word(word, dictionary, cache)
