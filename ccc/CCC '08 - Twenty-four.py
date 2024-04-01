import itertools
num = int(raw_input())
lists = ["{}{}{}{}{}{}{}","({}{}{}){}{}{}{}","{}{}({}{}{}){}{}","{}{}{}{}({}{}{})",
         "({}{}{}){}({}{}{})","({}{}{}{}{}){}{}","{}{}({}{}{}{}{})","(({}{}{}){}{}){}{}",
         "({}{}({}{}{})){}{}","{}{}(({}{}{}){}{})","{}{}({}{}({}{}{}))"]
numbers = list(itertools.product("+-*/", repeat = 3))

for i in xrange(num):
    a = float(raw_input())
    b = float(raw_input())
    c = float(raw_input())
    d = float(raw_input())
    cards = list(itertools.permutations([a,b,c,d], 4))
    check = 0
    maximum = 0
    for thing in lists:
        if check == 1:
            break
        for op in numbers:
            if check == 1:
                break
            for card in cards:
                if check == 1:
                    break
                string = thing.format(card[0],op[0],card[1],op[1],card[2],op[2],card[3])
                try:
                    num1 = eval(string)
                    num2 = int(str(num1).split(".")[0])
                except ZeroDivisionError:
                    continue
                if num1 == num2:
                    if num2 == 24:
                        check = 1
                    if num2 > maximum and num2 <= 24:
                        maximum = num2

    print maximum
