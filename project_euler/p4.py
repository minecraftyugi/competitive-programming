def is_palindrome(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if str_n[i] != str_n[len(str_n)-i-1]:
            return False

    return True

largest_palindrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i * j):
            largest_palindrome = max(largest_palindrome, i * j)

print(largest_palindrome)
