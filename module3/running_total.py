n,m=map(int,input().split())
y=list(map(int,input().strip().split()))[:n]
max1=0
for i in range(n):
    add1=0
    j=i
    for x in range(m):
        if j==n:
            j=0
        add1=add1+y[j]
        j+=1
    if add1>max1:
        max1=add1
print(max1)
