word = raw_input()

def permutations(s):
    """ (str) -> list of str

    Return a sorted list of all permutations of s.

    """

    ans = []
    if not s:
        ans.append("")
    else:
        previous = permutations(s[1:])
        for permutation in previous:
            for pos in xrange(len(permutation)):
                ans.append(permutation[:pos] + s[0] + permutation[pos:])

            ans.append(permutation + s[0])

    return sorted(ans)

for permutation in permutations(word):
    print permutation
