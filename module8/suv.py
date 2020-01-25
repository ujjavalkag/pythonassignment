from automobile import Automobile
class SUV(Automobile):
    def __init__(self,make,model,mileage,price,pass_cap):
        super().__init__(make,model,mileage,price)
        self.__pass_cap=pass_cap
    def set_pass_cap(self,pass_cap):
        self.__pass_cap=pass_cap
    def get_pass_cap(self):
        return self.__pass_cap
s1=SUV('india','i9','24km/l','80k$','none')
print('manufactured in:',s1.get_make())
print('model:',s1.get_model())
print('mileage:',s1.get_mileage())
print('price:',s1.get_price())
print('pass_cap:',s1.get_pass_cap())

    
        
        
