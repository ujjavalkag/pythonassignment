from numpy import *
arr1=array([
    [4,9,2],
    [3,5,7],
    [8,1,6]
    ])
'''
print(sum(diagonal(arr1)))
for i in range(0,3):
    print(sum(arr1[i]))
'''
if sum(diagonal(arr1))==sum(arr1[0])==sum(arr1[1])==sum(arr1[2]):
    print('magic square')
else:
    print('lo shu magic not shown')
