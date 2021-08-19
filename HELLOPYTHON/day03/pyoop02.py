class JindoDog:
    def __init__(self):
        self.power_bark = 0
        
    def train(self):    
        self.power_bark +=1

class SochoBird:
    def __init__(self):
        self.flag_fry = False
    
    def practice(self):
        self.flag_fly = True
      
      
class dogBird(JindoDog,SochoBird):
    def __init__(self):
        JindoDog.__init__(self)
        SochoBird.__init__(self)

dogbird = dogBird()        
print(dogbird.power_bark)
print(dogbird.flag_fry)
dogbird.train()
dogbird.practice()
print(dogbird.power_bark)
print(dogbird.flag_fly)
