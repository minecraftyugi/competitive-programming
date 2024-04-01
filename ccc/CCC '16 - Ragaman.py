from collections import *
c=Counter
a=c(raw_input())
b=c(raw_input())+c("*")
b.subtract(a)
[b.subtract(c("*"*-b[i]))for i in b if b[i]<0]
print"AN"[b["*"]<1]
