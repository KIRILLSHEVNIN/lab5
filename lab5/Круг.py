import math
 
 
class Круг:
 
    def __init__(self, r, col):
        self.col = col
        self.r = r
        self.площадь = self.r * math.pi
 
    def __repr__(self):
        return (self.col + ' круг с площадью ' + str(self.площадь))
 
