m = input()
n = input()
a = []
b = []

for i in xrange(n):
    a.append(raw_input())

for i in xrange(n):
    b.append(raw_input())

def possible(sequence, index, loops):
    if index == n and loops == 1:
        return 0, []
    if loops == m:
        index += 1
        sequence.pop()
        print sequence, index, loops, "Case 1"
        return possible(sequence, index, loops - 1)

    if index == n:
        index = sequence.pop() + 1
        #print sequence, index, loops, "Case 2"
        return possible(sequence, index, loops - 1)
    else:
        sequence.append(index)
        
    s1 = "".join(a[i]for i in sequence)
    s2 = "".join(b[i]for i in sequence)
    #print s1
    #print s2
    if s1 == s2:
        return loops, sequence
    elif len(s1) < len(s2):
        if s1 == s2[:len(s1)]:
            index = 0
            #print sequence, index, loops, "Case 3"
            return possible(sequence, index, loops + 1)
        else:
            index += 1
            sequence.pop()
            #print sequence, index, loops, "Case 4"
            return possible(sequence, index, loops)
    else:
        if s2 == s1[:len(s2)]:
            index = 0
            print sequence, index, loops, "Case 5"
            return possible(sequence, index, loops + 1)
        else:
            index += 1
            sequence.pop()
            #print sequence, index, loops, "Case 6"
            return possible(sequence, index, loops)
        
    return

if all(len(i)<len(j)for i in a for j in b)or all(len(i)<len(j)for i in b for j in a):
    print "No solution."
    raise SystemExit

ans = possible([], 0, 1)

if ans[0]:
    print ans[0]
    for pos in ans[1]:
        print pos + 1
else:
    print "No solution."

"""
13
3
aaaaaaaaaaaaaa
aaaaaaaaaaaaa
aaaaaaaaaaaa
aaaaaaaaaaa
aaaaaaaaaa
aaaaaaaaa
"""
