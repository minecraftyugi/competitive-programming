import sys

raw_input = sys.stdin.readline
t = int(raw_input())
def process(b):
    ones = []
    zeros = []
    prev = "1"
    count = 0
    for ch in b:
        if ch == prev:
            count += 1
        else:
            if prev == "1":
                ones.append(count)
            else:
                zeros.append(count)

            prev = ch
            count = 1

    if prev == "1":
        ones.append(count)
    else:
        zeros.append(count)

    if len(zeros) < len(ones):
        zeros.append(0)
        
    num = ones[0]
    if num == 1:
        ans = 1 #add 1
    elif num == 2:
        ans = 3 #add 1, shift 1, add 1 or add 1, add 1, add 1
    else:
        ans = 1 + num + 1 #add 1, shift num times, subtract 1

    ans += zeros[0]
    for i in xrange(1, len(ones)):
        ans += 1 #shift 1
        num = ones[i]
        if num == 1:
            ans += 1 #add 1
        elif num == 2:
            if zeros[i-1] == 1 and ones[i-1] >= 3:
                ans -= 1 #shouldve shifted one more
                
            ans += 3 #add 1, shift 1, add 1 or add 1, add 1, add 1
        else:
            ans -= 1 #no shift needed
            if zeros[i-1] == 1:
                if ones[i-1] >= 3:
                    ans -= 1 #shouldve shifted one more
                elif ones[i-1] == 2 and i-2 >= 0:
                    ans -= 1 #shouldve done something else
                    
            ans += 1 + num + 1 #add 1, shift num times, subtract 1

        ans += zeros[i]

    return ans

for i in xrange(t):
    n = int(raw_input())
    print process(bin(n)[2:])

"""
47574
76690
286792
129772
199553
111947
105211
288350625
522795290
885092931
740303375
997218214
1491936011664
13673260228259
1890762881626
230915767904
9039187325033873341
8921065283336787870
565587020176515884
"""
