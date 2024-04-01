import random
f = open("aplusb.txt", "w")
a1, a2, b1, b2 = "", "", "", ""
a1 += str(random.randint(0, 9))
a2 += str(random.randint(0, 9))
b1 += str(random.randint(0, 9))
b2 += str(random.randint(0, 9))

for i in xrange(6):
   a1 += str(random.randint(1, 9))
   b1 += str(random.randint(1, 9))
   b2 += str(random.randint(1, 9))

for i in xrange(4):
    a2 += str(random.randint(1, 9))
    
f.write("20\n")

f.write(a1+" "+a2+"\n")
f.write(a2+" "+a1+"\n")
f.write("-"+a1+" "+a2+"\n")
f.write("-"+a2+" "+a1+"\n")
f.write(a1+" "+a2+"\n")
f.write(a2+" "+a1+"\n")
f.write(a1+" "+"-"+a2+"\n")
f.write(a2+" "+"-"+a1+"\n")
f.write("-"+a1+" "+"-"+a2+"\n")
f.write("-"+a2+" "+"-"+a1+"\n")

f.write(b1+" "+b2+"\n")
f.write(b2+" "+b1+"\n")
f.write("-"+b1+" "+b2+"\n")
f.write("-"+b2+" "+b1+"\n")
f.write(b1+" "+b2+"\n")
f.write(b2+" "+b1+"\n")
f.write(b1+" "+"-"+b2+"\n")
f.write(b2+" "+"-"+b1+"\n")
f.write("-"+b1+" "+"-"+b2+"\n")
f.write("-"+b2+" "+"-"+b1+"\n")

f.close()

f = open("aplusb.txt", "r")
n = int(f.readline().strip())

for i in xrange(n):
    a, b = map(int, f.readline().strip().split())
    print a + b

f.close()
