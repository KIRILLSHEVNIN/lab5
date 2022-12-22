class Прямоугольник:
 
    def __init__(self, c, b, col):
        self.col = col
        self.c = c
        self.b = b
        self.площадь = self.c*self.b
 
 
    def __repr__(self):
        return (self.col + ' прямоугольник с площадью ' + str(self.площадь))
