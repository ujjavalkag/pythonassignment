x=list(map(int,input().strip().split()))

x.sort()
y=set(x)
c=list(y)
c.sort()
d=[]
for t in c:
    d.append(x.count(t))
for f in range(len(d)):
    for k in range(max(d)):
        print(c[d.index(max(d))],end=' ')
    d[d.index(max(d))]=-1
