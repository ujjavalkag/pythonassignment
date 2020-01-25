x=int(input('number of packgaes purchased:'))
price=x*99
discount=0
if x>10 and x<19:
    discount=price*0.1
if x>20 and x<49:
    discount=price*0.2
if x>50 and x<99:
    discount=price*0.3
if x>100:
    discount=price*0.4
if discount!=0:    
        print('discount:',discount)
print('price',price-discount)        
    
        
