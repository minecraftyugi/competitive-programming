n = input()
k = input()
dp = [[-1]*251 for i in xrange(251)]

def num_pies(pies, people):
    if pies == 0:
        dp[pies][people] = 0
    elif pies < 0:
        return 0
    elif dp[pies][people] == -1:
        if people == 1:
            dp[pies][people] = 1
        else:
            dp[pies][people] = 0
            dp[pies][people] += num_pies(pies-1, people-1) + \
                                num_pies(pies-people, people)

    return dp[pies][people]

print num_pies(n, k)
