l1=[1,2,3,6,8,4]
l2=[2,4,1,3,8]
if len(l1)==len(l2):
    print('all element is present')
else:
    for x in l1:
        if x not in l2:
            print(x,'not present in l2')
'''
print(sum(l1)-sum(l2))
