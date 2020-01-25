class car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return f'a {self.color} car'
c1=car('red',100)
print(c1)





        
