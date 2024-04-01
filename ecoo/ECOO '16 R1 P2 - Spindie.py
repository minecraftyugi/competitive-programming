for i in xrange(10):
  n = input()
  numbers = set(map(int, raw_input().split()))
  possible = map(int, raw_input().split())
  total = set()
  ans = ""

  for number1 in numbers:
    for number2 in numbers:
      total.add(number1*number2)
      total.add(number1+number2)
  
  for thing in possible:
    check = 0
    for number in numbers:
      check1 = thing*1.0/number
      check2 = thing-number
      if check1 == int(check1):
        if int(check1) in total:
          ans += "T"
          check = 1
          break
      if check2 in total:
        ans += "T"
        check = 1
        break


    if check == 0: ans += "F"

  print ans
