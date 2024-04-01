n = int(input())
balls = list(map(int, input().split()))
dp = [[-1]*(n+1) for _ in range(n+1)]

def can_merge(start, end):
    """ (int, int) -> bool

    Return True iff balls[start:end] can be merged. 
    Precondition: 0 <= start <= end <= n  
    """
    
    if start >= end - 1:
        return True

    left = start + 1
    right = end - 1
    left_sum = balls[left - 1]
    right_sum = balls[right]
    valid = False
    while left <= right:
        if left_sum == right_sum:
            if dp[start][left] == -1:
                dp[start][left] = can_merge(start, left)
            if dp[left][right] == -1:
                dp[left][right] = can_merge(left, right)
            if dp[right][end] == -1:
                dp[right][end] = can_merge(right, end)
                
            valid |= dp[start][left] * dp[left][right] * dp[right][end]
            left += 1
            left_sum += balls[left - 1]
        elif left_sum > right_sum:
            right -= 1
            right_sum += balls[right]
        else:
            left += 1
            left_sum += balls[left - 1]

    return valid

ans = 0
for i in range(n):
    for j in range(i+1, n+1):
        if can_merge(i, j):
            ans = max(ans, sum(balls[i:j]))

print(ans)
