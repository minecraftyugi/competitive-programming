letters = [0]+[chr(i)for i in xrange(97, 123)]
n = input()
m = 2 * n - 1
matrix = [[0 for i in xrange(m)]for i in xrange(m)]

for i in xrange(1, n+1):
    top = n - i
    bottom = n + i - 2
    left = n - i
    right = n + i - 2
    for j in xrange(1, i+1):
        matrix[top][n-j] = letters[i]
        matrix[top][n+j-2] = letters[i]
        matrix[bottom][n-j] = letters[i]
        matrix[bottom][n+j-2] = letters[i]
        matrix[n-j][left] = letters[i]
        matrix[n+j-2][left] = letters[i]
        matrix[n-j][right] = letters[i]
        matrix[n+j-2][right] = letters[i]

for i in matrix:
    print "".join(i)
