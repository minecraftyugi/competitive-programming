w=sum;x=raw_input;y=map;z=int
a=y(z,x().split())
b=y(z,x().split())
c=y(z,x().split())
d=y(z,x().split())
print["not ",""][w(a)==w(b)==w(c)==w(d)and all(w(i)==w(a)for i in zip(a,b,c,d))]+"magic"
