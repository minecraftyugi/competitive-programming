q=input()
n=range(input())
x=sorted(map(int,raw_input().split()))
y=sorted(map(int,raw_input().split()))
q-2or y.reverse()
print sum([max(x[i],y[i])for i in n])