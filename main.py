from lab5.Прямоугольник import *
from lab5.Круг import *
from lab5.Квадрат import *
 
def main():
    x = 0
    print('Введите цвет фигуры')
    col = input()
    print('Введите название фигуры (прямоугольник, круг, квадрат)')
    f = input()
    if f == 'прямоугольник':
        print('Введите ширину прямоугольника')
        c = int(input())
        print('Введите длину прямоугольника')
        b = int(input())
        x = Прямоугольник(c, b, col)
    if f == 'круг':
        print('Введите радиус круга')
        r = int(input())
        x = Круг(r, col)
    if f == 'квадрат':
        print('Введите сторону квадрата')
        a = int(input())
        x = Квадрат(a, col)
    print(x)
 
 
 
 
if __name__ == "__main__":
    main()
