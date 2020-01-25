list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=[]
for x in list1:
    for y in range(len(x)):
        list2.append(x[y])
print(list2)    
