n = input("Enter the number of equations: ")
print "The letters correspond to the congruence ax = b (mod c)"
equations = []
mList = []
M = 1

for i in xrange(1,n+1):
    a = input("Enter a value for equation "+str(i)+": ")
    b = input("Enter b value for equation "+str(i)+": ")
    c = input("Enter c value for equation "+str(i)+": ")
    equations.append([a,b,c])
    M *= c

for index, thing in enumerate(equations):
    a, b, c = thing
    if a == 1:
        print "Equation {}: x = {} (mod {})".format(index, b, c)
        continue
    else:
        i = 1
        while 1:
            if (c*i + b) % a == 0:
                print "Equation {}: {}x = {} + {}({})(mod {})".format(index, a, b, c, i, c)
                num = (c*i + b) / a
                print "Equation {}: x = {} (mod {})".format(index, num, c)
                equations[index] = [1, num, c]
                break
            else:
                i += 1

for i in range(1000):
    if (7*i + 1) % 143 == 0:
        print i
        break

print equations
"""
2x = 5 mod 7
3x = 4 mod 11
5x = 9 mod 13
"""
