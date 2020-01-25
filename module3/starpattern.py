x=int(input('enter odd value:'))
for i in range(x):
    for j in range(x-i):
        print('*',end='')
    print()
for i in range(x-1):
    for j in range(i+2):
        print('*',end='')
    print()
    
x=int(input('enter odd value:'))
print(' ')
for i in range(x-1):
    for j in range(x):
        if j==(x//2):
            print('*')    
        else:
            print('  ',end='')
    print(' ')        
    if i==x//2-1:
        for k in range(x):
            print('* ',end='')
        print()    
    

y=int(input('enter any number'))
for i in range(y):
    for j in range(y-i):
        print(' ',end='')  
    for k in range(i+1):
        print('* ',end='')
    print()    
for i in range(y):
    print(' ',end='')
    for j in range(i):
        print(' ',end='')
    for k in range(y-i-1):
        print(' *',end='')
    print()  

y=int(input('enter any number'))
for i in range(y):
    for j in range(y-i):
        print(' ',end='')  
    for k in range(i+1):
        if k==0 or k==i:
           print(' *',end='')
      
        else:
           print('  ',end='')
    print()
for g in range(y+1):
    print(' *',end='')
 
