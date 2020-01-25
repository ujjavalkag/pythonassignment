x=list(map(str,input().strip().split()))
y=set(x)
z=list(y)
z.sort()
for i in z:
    print(i,end=' ')

