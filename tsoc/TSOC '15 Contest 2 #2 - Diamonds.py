n=input()
a=["*"for i in range(n)]
print`a`[2::5]
for i in range(n/2):
    a[n/2+i]=" "
    a[n/2-i]=" "
    print`a`[2::5]
for i in range(n/2-1,-1,-1):
    a[n/2+i]="*"
    a[n/2-i]="*"
    print`a`[2::5]
