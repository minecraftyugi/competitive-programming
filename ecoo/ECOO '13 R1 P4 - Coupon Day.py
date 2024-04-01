for i in xrange(5):
    n = input()
    prices = []
    coupons = []
    
    for j in xrange(n):
        prices.append(float(raw_input()))

    c = input()

    for j in xrange(c):
        prices.append(raw_input())
