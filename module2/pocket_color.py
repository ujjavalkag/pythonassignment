x=int(input('number of pocket:'))
if x==0:
    print('pocket is green')
elif (x>0 and x<=10) or (x>=19 and x<=28):
    if x%2==0:
        print('pocket is black')
    else:
        print('pocket is red')
elif (x>=11 and x<=18)or(x>=29 and x<=36):
    if x%2==0:
        print('pocket is red')
    else:
        print('pocket is black')
else:
    print('invalid pocket number is choosen')
        
    
        
    
