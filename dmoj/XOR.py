t = input()

for i in xrange(t):
    a, b = map(int, raw_input().split())
    num1 = [a-1,1,a,0][(a-1)%4]
    num2 = [b,1,b+1,0][b%4]
    print num1 ^ num2

