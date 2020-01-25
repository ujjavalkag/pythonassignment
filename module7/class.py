import random
class bhalu:
    def __init__(self):
        self.sideup='Heads'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup='Heads'
        else:
            self.sideup='Tails'
    def get_sideup(self):
        return self.sideup
c1=bhalu()
c1.toss()
print(c1.get_sideup())





        
