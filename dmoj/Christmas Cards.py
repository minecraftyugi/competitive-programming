import sys, pprint

raw_input = sys.stdin.readline
n = input()
dp = [[0]*n for i in xrange(n)]
hand = [0]*n
mana = [0]*n
cards = [0]*n
for i in xrange(n):
    c, d = map(int, raw_input().split())
    mana[i] = c
    cards[i] = d

#dp[0] = mana[0]
hand[0] = 1
start = cards[0]
for i in xrange(start):
    dp[i+1][start+1] = mana[0]
    
for i in xrange(1, n):
    go = cards[i]
    val = mana[i]
    #print dp, hand
    pprint.pprint(dp)
    for j in xrange(n):
        dist = min(j + go, n-1)
        upto = dist if dist == j+go else n
        if dp[i][j]:
            for k in xrange(j, upto):
                if dp[k][dist] == 0:
                    dp[k][dist] = dp[i][j] + val
                else:
                    dp[k][dist] = min(dp[k][dist], dp[i][j] + val)
    
##    for j in xrange(hand[i], min(hand[i]+go, n)):
##        if dp[j] == 0:
##            dp[j] = dp[i] + val
##            hand[j] = hand[i] + go
##        else:
##            if dp[i] + val <= dp[j]:
##                dp[j] = dp[i] + val
##                hand[j] = hand[i] + go

    #print dp, hand, go, val
    pprint.pprint(dp)
    print "I:", i, go, val
    print

print dp[-1][-1]
