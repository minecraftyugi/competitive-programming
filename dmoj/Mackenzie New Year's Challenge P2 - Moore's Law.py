import math
n = float(raw_input())
start = 2
lists = []

num = n / start
num = math.log(num) / math.log(start)
num = num * (365 * 2) #730 days to double
num = int(math.ceil(num))

years = num / 365
num -= years * 365
if years > 0:
    lists.append(`years` + "Y")
    
months = num / 30
num -= months * 30
if months > 0:
    lists.append(`months` + "M")
    
weeks = num / 7
num -= weeks * 7
if weeks > 0:
    lists.append(`weeks` + "W")
    
days = num
if days > 0:
    lists.append(`days` + "D")

if lists == []:
    print "Now!"
else:
    print " ".join(lists)
