# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        '''
        определяем длину сторон с помощью формул векторов
        '''
        self.ab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.bc = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        self.ac = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    def p(self):
        '''
        определяем периметр
        '''
        return self.ab + self.bc + self.ac

    def s(self):
        '''
        определяем площадь с помощью формулы Герона
        '''
        return round(math.sqrt(self.p()/2 * (self.p()/2 - self.ab) * (self.p()/2 - self.bc) * (self.p()/2 - self.ac)), 2)

    def h(self, side):
        '''
        определяем длину высоты, опущенной на сторону side (второй параметр)
        '''
        return round((2 * self.s()) / side, 2)
