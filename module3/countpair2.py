from itertools import *

def countpair(list3):
    for x in list3:
        if sum(x)==sum1:
            print(x)
    
n=int(input('number of elements:'))
sum1=int(input('enter sum value:'))
a=list(map(int,input().strip().split()))[:n]
b=list(map(int,input().strip().split()))[:n]
list1=list(combinations(a,2))
list2=list(combinations(b,2))           
countpair(list1)
countpair(list2)
