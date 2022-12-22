from lab5.Прямоугольник import *
 
 
class Квадрат(Прямоугольник):
 
    def __init__(self, a, col):
        super().__init__(a, a, col)
 
 
    def __repr__(self):
        return (self.col + ' квадрат с площадью ' + str(self.площадь))
