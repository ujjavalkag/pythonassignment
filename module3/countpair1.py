from itertools import *
#list1=[]
n=int(input('number of elements:'))
sum1=int(input('enter sum value:'))
a=list(map(int,input().strip().split()))[:n]
list1=list(combinations(a,2))
for x in list1:
    if sum(x)==sum1:
        print(x)

