from automobile import Automobile
class car(Automobile):
    def __init__(self,make,model,mileage,price,doors):
        super().__init__(make,model,mileage,price)
        self.__doors=doors
    def set_doors(self,doors):
        self.__doors=doors
    def get_doors(self):
        return self.__doors
s1=car('india','i8','100','1M$','automatic censored')
print('manufactured in:',s1.get_make())
print('model:',s1.get_model())
print('mileage:',s1.get_mileage())
print('price:',s1.get_price())
print('doors:',s1.get_doors())        
        
