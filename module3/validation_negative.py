import sys
while(1):
    print('1.calculate,2.exit')
    x=int(input('choice'))
    if x==1:
        y=int(input('enter wholesale  price:'))
        while y<0:
            print('invalid number enterd:')
            y=int(input('enter wholesale  price:'))
        
        print("retail price:",y*0.5)
    else:
        sys.exit(x)
