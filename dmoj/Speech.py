n=raw_input;d={}
exec"a,b=n().split();d[b]=a;"*int(n())
m=n().split();m[-1]=m[-1][:-1]
print" ".join([d[y]if y in d else m[x]for x,y in enumerate(m)])+"."
