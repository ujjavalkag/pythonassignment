from automobile import Automobile
class Truck(Automobile):
    def __init__(self,make,model,mileage,price,drive_type):
        super().__init__(make,model,mileage,price)
        self.__drive_type=drive_type
    def set_drive_type(self,drive_type):
        self.__drive_type=drive_type
    def get_drive_type(self):
        return self.__drive_type

s1=Truck('india','i9','24km/l','80k$','all india permit')
print('manufactured in:',s1.get_make())
print('model:',s1.get_model())
print('mileage:',s1.get_mileage())
print('price:',s1.get_price())
print('driver:',s1.get_drive_type())
