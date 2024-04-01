from math import floor

for i in xrange(10):
  t, a, p, q = map(float, raw_input().split())
  n = input()
  count = 0
  for i in range(n):
    t1, a1, p1, q1 = map(float, raw_input().split())
    if floor((t*t1 + a*a1+ p*p1 + q*q1)/100)>=50:
      count += 1
  print count
    
